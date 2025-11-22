# Scripts de GCP en Java - Guía Rápida

## Requisitos previos

- Java 17 o superior  
- Maven 3.x  
- Credenciales de servicio de GCP (archivo JSON)

## Preparación

### 1. Compilar el proyecto

Desde la carpeta `java`:

```bash
mvn clean package
```

Esto generará un `.jar` ejecutable en `target/`.

### 2. Configurar credenciales

1. Solicita tus credenciales de equipo (un archivo `.json`)  
2. Guárdalo en una ruta accesible, por ejemplo:  
   `E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json`

## Uso

En todos los ejemplos, asume que estás en la carpeta `java` y que ya has compilado el proyecto.

```bash
mvn exec:java -Dexec.mainClass="org.eurecat.Main" -Dexec.args="<AQUÍ_LOS_FLAGS>"
```

> Sustituye `<AQUÍ_LOS_FLAGS>` por uno de los ejemplos siguientes.

### 1. Crear instancia

```bash
mvn exec:java -Dexec.mainClass="org.eurecat.Main" ^
  -Dexec.args="--credentials E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json --project-id hackeps2025-team1 --create-instance --zone europe-west1-b --machine-type e2-highcpu-4 --name test-java"
```

**Parámetros principales:**
- `--credentials`: Ruta al archivo de credenciales JSON  
- `--project-id`: ID del proyecto de GCP (`hackeps2025-team1`)  
- `--zone`: Zona donde se creará la instancia (ej: `europe-west1-b`)  
- `--machine-type`: Tipo de máquina (ej: `e2-highcpu-4`)  
- `--name`: Nombre de la instancia  

### 2. Listar instancias

```bash
mvn exec:java -Dexec.mainClass="org.eurecat.Main" ^
  -Dexec.args="--credentials E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json --project-id hackeps2025-team1 --list-instances --zone europe-west1-b"
```

**Nota:** Si vuestro `Main` permite omitir `--zone`, podríais listar todas las instancias de todas las zonas simplemente quitando ese flag.

### 3. Borrar instancia

```bash
# Borrar instancia buscando en todas las zonas
mvn exec:java -Dexec.mainClass="org.eurecat.Main" ^
  -Dexec.args="--credentials E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json --project-id hackeps2025-team1 --delete-instance --name test-java"

# Borrar instancia especificando la zona
mvn exec:java -Dexec.mainClass="org.eurecat.Main" ^
  -Dexec.args="--credentials E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json --project-id hackeps2025-team1 --delete-instance --name test-java --zone europe-west1-b"
```

### 4. Buscar tipos de instancia

```bash
mvn exec:java -Dexec.mainClass="org.eurecat.Main" ^
  -Dexec.args="--credentials E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json --project-id hackeps2025-team1 --find-instance --zone europe-west1-b --region europe-west1-b --cpus 4 --ram 4"
```

**Parámetros:**
- `--cpus`: Número mínimo de CPUs requeridas  
- `--ram`: Cantidad mínima de RAM en GB  

Este comando te ayuda a encontrar tipos de máquinas que cumplan con tus requisitos de CPU y RAM para esa región/zona.

## Uso con IntelliJ IDEA

Si prefieres ejecutar el proyecto desde IntelliJ:

1. **Importa el proyecto** como proyecto Maven (`File > Open` y selecciona la carpeta `java`).  
2. Espera a que IntelliJ descargue las dependencias de Maven.  
3. Crea una **Run Configuration**:
   - Ve a `Run > Edit Configurations...`  
   - Pulsa en `+` y elige **Application**  
   - En **Main class** pon: `org.eurecat.Main`  
   - En **Use classpath of module** selecciona el módulo `java` (o el que corresponda)  
   - En **Program arguments** pega los flags que quieras usar, por ejemplo:  
     ```text
     --credentials E:\WORK\hackeps\examples\google-cloud-platform\google-cloud-credentials.json --project-id hackeps2025-team1 --create-instance --zone europe-west1-b --machine-type e2-highcpu-4 --name test-java --ssh-key "latra:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDEJjzb3S6r5QQC0/GTxROAyvZ+lLGwqBCyUEvJgI+KNWD26WctvLcnp4LhK8wLnQIk9M/lqxsYqiw6QYIG+3TNAKm6XPyTCTjleKxNCIf57iH1K9htGpp9BzxppkFNJkdhaPJOhxkgskTSTpciRwEyxIMiKI4Rh4f5r9dgWd4gUrqLvN7nuAndPlzbbTdk2fiSG8vibs+cHhgQdeop85io6v0N92sJQkqOp5k8bbKistSHQMMjl2ql6/6icR3Abtryym5d4EG4eAZMzGunCs0h0CB62I8HkQ9HxVAAP26eIW9+nkTbD/H0rYXFjZXCKaWbMx6uXOiMPwan05/Ux+LE43Eek5mcxATuRZlNfdORS9vKM+57o4MClTFxledFviEhWIu4yVVoJhCLdfQjBKsN1h11RVHs/53kS0N7O9sFX3J68llHRWdOhVKHtbmYN8ZwRh1Z6lO/Rc/5bCJhfrV3z1ufO0ANSzWBTHxx4e/YqNkSKy5aINkZInqiL1OpCe4khEe1L4clZ3kEpzZ3i532/PWYyd+APXecr1KIM6AMHzltb5e+CfunO7zw6GBzf1/bTyph8NALsqpMS9tL3BjDXrrK+Byq+oD2VrHO9fJ6TswlyuN2GPG0r5bh3HCSygoxL6BOhDI/DCcbepsvpW3ikMXMWaJyBr9stfuPRQyUhw=="
     ```
4. Aplica los cambios y ejecuta con el botón de **Run** (o `Shift+F10`).

