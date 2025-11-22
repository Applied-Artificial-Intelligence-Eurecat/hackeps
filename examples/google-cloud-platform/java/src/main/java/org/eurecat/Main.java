package org.eurecat;
// Main.java
import com.google.api.gax.core.FixedCredentialsProvider;
import com.google.auth.oauth2.ServiceAccountCredentials;
import com.google.cloud.compute.v1.*;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutionException;

public class Main {
    private static FixedCredentialsProvider credentialsProvider;

    public static void main(String[] args) throws Exception {
        Map<String, String> p = parseArgs(args);

        // Equivalente a --credentials en Python:
        // Aquí SOLO lo leemos para información; la autenticación real
        // se hace con GOOGLE_APPLICATION_CREDENTIALS en el entorno.
        String credentialsPath = p.get("credentials");
        if (credentialsPath == null) {
            System.err.println("--credentials es obligatorio (debe apuntar al JSON usado en GOOGLE_APPLICATION_CREDENTIALS)");
            return;
        }
        credentialsProvider = FixedCredentialsProvider.create(
                ServiceAccountCredentials.fromStream(new FileInputStream(credentialsPath))
        );


        boolean findInstance    = p.containsKey("find-instance");
        boolean createInstance  = p.containsKey("create-instance");
        boolean listInstances   = p.containsKey("list-instances");
        boolean deleteInstance  = p.containsKey("delete-instance");

        if (!findInstance && !createInstance && !listInstances && !deleteInstance) {
            System.out.println("Debes indicar una acción: --find-instance | --create-instance | --list-instances | --delete-instance");
            return;
        }

        String projectId   = p.get("project-id");   // en Python lo lees del JSON; aquí pásalo directamente
        String zone        = p.get("zone");
        String region      = p.get("region");
        String machineType = p.get("machine-type");
        String name        = p.get("name");
        String sshKey      = p.get("ssh-key");
        Integer cpus       = p.containsKey("cpus") ? Integer.parseInt(p.get("cpus")) : null;
        Integer ramGb      = p.containsKey("ram")  ? Integer.parseInt(p.get("ram"))  : null;

        if (projectId == null) {
            System.err.println("--project-id es obligatorio (ID del proyecto de GCP)");
            return;
        }

        if (findInstance) {
            if (region == null || zone == null || cpus == null || ramGb == null) {
                System.err.println("--find-instance requiere --region, --zone, --cpus y --ram");
                return;
            }
            findInstanceTypes(projectId, region, zone, cpus, ramGb);
        } else if (createInstance) {
            if (name == null || machineType == null || zone == null) {
                System.err.println("--create-instance requiere --name, --machine-type y --zone");
                return;
            }
            createInstance(projectId, zone, name, machineType, sshKey);
        } else if (listInstances) {
            listInstances(projectId, zone);
        } else if (deleteInstance) {
            if (name == null) {
                System.err.println("--delete-instance requiere --name");
                return;
            }
            if (zone != null) {
                deleteInstance(projectId, zone, name);
            } else {
                findAndDeleteInstance(projectId, name);
            }
        }
    }

    // Parser muy simple para flags tipo --clave valor
    private static Map<String, String> parseArgs(String[] args) {
        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < args.length; i++) {
            String a = args[i];
            if (a.startsWith("--")) {
                String key = a.substring(2);
                String value = "true";
                if (i + 1 < args.length && !args[i + 1].startsWith("--")) {
                    value = args[++i];
                }
                map.put(key, value);
            }
        }
        return map;
    }

    // ===================== LISTAR INSTANCIAS =====================

    private static void listInstances(String projectId, String zone) throws IOException {
        InstancesSettings settings = InstancesSettings.newBuilder()
                .setCredentialsProvider(credentialsProvider)
                .build();
        try (InstancesClient instancesClient = InstancesClient.create(settings)) {
            if (zone != null) {
                System.out.printf("Listando instancias en la zona: %s%n%n", zone);
                for (Instance instance : instancesClient.list(projectId, zone).iterateAll()) {
                    printInstance(instance, zone);
                }
            } else {
                System.out.println("Listando instancias en todas las zonas...\n");
                try (ZonesClient zonesClient = ZonesClient.create()) {
                    int total = 0;
                    for (Zone z : zonesClient.list(projectId).iterateAll()) {
                        String zoneName = z.getName();
                        Iterable<Instance> it = instancesClient.list(projectId, zoneName).iterateAll();
                        boolean any = false;
                        for (Instance inst : it) {
                            if (!any) {
                                System.out.printf("═══ Zona: %s ═══%n", zoneName);
                                any = true;
                            }
                            printInstance(inst, zoneName);
                            total++;
                        }
                    }
                    if (total == 0) {
                        System.out.println("No se encontraron instancias en el proyecto.");
                    } else {
                        System.out.printf("%nTOTAL: %d instancia(s) en el proyecto%n", total);
                    }
                }
            }
        }
    }

    private static void printInstance(Instance instance, String zone) {
        String status = instance.getStatus();
        String emoji;
        if ("RUNNING".equals(status)) emoji = "🟢";
        else if ("TERMINATED".equals(status)) emoji = "🔴";
        else emoji = "🟡";

        System.out.printf("%s Nombre: %s%n", emoji, instance.getName());
        System.out.printf("   Estado: %s%n", status);
        String mt = instance.getMachineType();
        if (mt != null && mt.contains("/")) {
            mt = mt.substring(mt.lastIndexOf('/') + 1);
        }
        System.out.printf("   Tipo de máquina: %s%n", mt);
        System.out.printf("   Zona: %s%n", zone);

        for (NetworkInterface ni : instance.getNetworkInterfacesList()) {
            if (!ni.getNetworkIP().isEmpty()) {
                System.out.printf("   IP interna: %s%n", ni.getNetworkIP());
            }
            for (AccessConfig ac : ni.getAccessConfigsList()) {
                if (!ac.getNatIP().isEmpty()) {
                    System.out.printf("   IP pública: %s%n", ac.getNatIP());
                }
            }
        }

        System.out.println();
    }

    // ===================== CREAR INSTANCIA =====================

    private static void createInstance(String projectId, String zone, String name,
                                       String machineType, String sshKey)
            throws IOException, ExecutionException, InterruptedException {

        if (sshKey == null) {
            sshKey = "";
        }
        System.out.printf("Creando instancia '%s' en zona %s (%s)%n", name, zone, machineType);
        InstancesSettings settings = InstancesSettings.newBuilder()
                .setCredentialsProvider(credentialsProvider)
                .build();
        try (InstancesClient instancesClient = InstancesClient.create(settings)) {
            String machineTypeUrl = String.format("zones/%s/machineTypes/%s", zone, machineType);

            AttachedDiskInitializeParams initParams = AttachedDiskInitializeParams.newBuilder()
                    .setSourceImage("projects/debian-cloud/global/images/family/debian-11")
                    .setDiskSizeGb(10L)
                    .build();

            AttachedDisk bootDisk = AttachedDisk.newBuilder()
                    .setBoot(true)
                    .setAutoDelete(true)
                    .setInitializeParams(initParams)
                    .build();

            AccessConfig accessConfig = AccessConfig.newBuilder()
                    .setName("External NAT")
                    .setType("ONE_TO_ONE_NAT")
                    .build();

            NetworkInterface networkInterface = NetworkInterface.newBuilder()
                    .setName("global/networks/default")
                    .addAccessConfigs(accessConfig)
                    .build();

            Instance.Builder instanceBuilder = Instance.newBuilder()
                    .setName(name)
                    .setMachineType(machineTypeUrl)
                    .addDisks(bootDisk)
                    .addNetworkInterfaces(networkInterface)
                    .setMetadata(Metadata.newBuilder().addItems(Items.newBuilder().setKey("ssh-keys").setValue(sshKey).build()));



            Instance instance = instanceBuilder.build();

            Operation operation = instancesClient.insertAsync(projectId, zone, instance).get();
            if (operation.hasError()) {
                System.out.println("❌ Error al crear la instancia:");
                operation.getError().getErrorsList().forEach(
                        e -> System.out.printf("  - %s: %s%n", e.getCode(), e.getMessage())
                );
            } else {
                System.out.printf("✅ Instancia '%s' creada correctamente%n", name);
            }
        }
    }

    // ===================== BORRAR INSTANCIA =====================

    private static boolean deleteInstance(String projectId, String zone, String name)
            throws IOException, ExecutionException, InterruptedException {
        InstancesSettings settings = InstancesSettings.newBuilder()
                .setCredentialsProvider(credentialsProvider)
                .build();
        try (InstancesClient instancesClient = InstancesClient.create(settings)) {
            System.out.printf("Verificando instancia '%s' en zona %s...%n", name, zone);
            try {
                Instance instance = instancesClient.get(projectId, zone, name);
                System.out.printf("✓ Instancia encontrada: %s (%s)%n",
                        instance.getName(), instance.getStatus());
            } catch (Exception e) {
                System.out.printf("❌ La instancia '%s' no existe en la zona %s%n", name, zone);
                return false;
            }

            System.out.println("Enviando solicitud de borrado...");

            Operation op = instancesClient.deleteAsync(projectId, zone, name).get();
            if (op.hasError()) {
                System.out.println("❌ Error al borrar la instancia:");
                op.getError().getErrorsList().forEach(
                        e -> System.out.printf("  - %s: %s%n", e.getCode(), e.getMessage())
                );
                return false;
            }

            System.out.printf("✅ Instancia '%s' borrada correctamente%n", name);
            return true;
        }
    }

    private static boolean findAndDeleteInstance(String projectId, String name)
            throws IOException, ExecutionException, InterruptedException {

        System.out.printf("Buscando instancia '%s' en todas las zonas...%n", name);
        InstancesSettings settings = InstancesSettings.newBuilder()
                .setCredentialsProvider(credentialsProvider)
                .build();
        ZonesSettings settingsZone = ZonesSettings.newBuilder().
                setCredentialsProvider(credentialsProvider)
                .build();
        try (InstancesClient instancesClient = InstancesClient.create(settings);
             ZonesClient zonesClient = ZonesClient.create(settingsZone)) {

            for (Zone z : zonesClient.list(projectId).iterateAll()) {
                String zoneName = z.getName();
                try {
                    Instance inst = instancesClient.get(projectId, zoneName, name);
                    System.out.printf("✓ Instancia encontrada en zona %s (%s)%n",
                            zoneName, inst.getStatus());
                    return deleteInstance(projectId, zoneName, name);
                } catch (Exception ignored) {
                    // No está en esta zona, seguimos
                }
            }
        }

        System.out.printf("❌ La instancia '%s' no se encontró en ninguna zona%n", name);
        return false;
    }

    // ===================== BUSCAR TIPOS DE INSTANCIA =====================

    private static void findInstanceTypes(String projectId, String region, String zone,
                                          int minCpus, int minRamGb) throws IOException {

        System.out.printf("Buscando tipos de máquina en %s que tengan >= %d CPU(s) y >= %d GB RAM%n",
                zone, minCpus, minRamGb);
        MachineTypesSettings settings = MachineTypesSettings.newBuilder()
                .setCredentialsProvider(credentialsProvider)
                .build();
        try (MachineTypesClient mtClient = MachineTypesClient.create(settings)) {
            for (MachineType mt : mtClient.list(projectId, zone).iterateAll()) {
                int cpus = mt.getGuestCpus();
                int ramGb = (int) Math.round(mt.getMemoryMb() / 1024.0);

                if (cpus == minCpus && ramGb == minRamGb) {
                    System.out.printf("- %s | %d vCPU | %d GB RAM%n",
                            mt.getName(), cpus, ramGb);
                }
            }
        }
    }
}