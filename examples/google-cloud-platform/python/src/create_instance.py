#!/usr/bin/env python3
"""
Script simple para crear una instancia de GCP
"""
import argparse
import json
import os
from google.cloud import compute_v1


def create_instance(project_id, zone, instance_name, machine_type, ssh_key=None):
    """
    Crea una instancia de GCP
    
    Args:
        project_id: ID del proyecto de GCP
        zone: Zona de GCP (ej: us-central1-a)
        instance_name: Nombre de la instancia a crear
        machine_type: Tipo de máquina (ej: e2-medium, n1-standard-1)
        ssh_key: Clave SSH pública para acceso (opcional)
    """
    print(f"Creando instancia '{instance_name}' en zona: {zone}")
    print(f"Tipo de máquina: {machine_type}")
    if ssh_key:
        print(f"Clave SSH: configurada")    
    
    # Cliente de compute
    instance_client = compute_v1.InstancesClient()
    
    # Configurar la instancia
    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
    
    # Configurar el disco de arranque (Debian 11)
    disk = compute_v1.AttachedDisk()
    disk.boot = True
    disk.auto_delete = True
    disk.initialize_params = compute_v1.AttachedDiskInitializeParams()
    disk.initialize_params.source_image = "projects/debian-cloud/global/images/family/debian-11"
    disk.initialize_params.disk_size_gb = 10
    instance.disks = [disk]
    
    # Configurar la red - os recomendamos dejar la red por defecto
    network_interface = compute_v1.NetworkInterface()
    network_interface.name = "global/networks/default"
    access_config = compute_v1.AccessConfig()
    access_config.name = "External NAT"
    access_config.type_ = "ONE_TO_ONE_NAT"
    network_interface.access_configs = [access_config]
    
    instance.network_interfaces = [network_interface]
    
    # Configurar metadata (SSH keys)
    if ssh_key:
        metadata = compute_v1.Metadata()
        metadata_item = compute_v1.Items()
        metadata_item.key = "ssh-keys"
        metadata_item.value = ssh_key
        metadata.items = [metadata_item]
        instance.metadata = metadata
        
    try:
        # Crear la instancia
        request = compute_v1.InsertInstanceRequest()
        request.project = project_id
        request.zone = zone
        request.instance_resource = instance

        print("\nEnviando solicitud de creación...")
        operation = instance_client.insert(request=request)

        print(f"Operación iniciada: {operation.name}")
        print("Esperando a que se complete la operación...")

        # Esperar a que se complete la operación
        operation_client = compute_v1.ZoneOperationsClient()
        while operation.status != compute_v1.Operation.Status.DONE:
            operation = operation_client.get(
                project=project_id,
                zone=zone,
                operation=operation.name
            )

        if operation.error:
            print(f"\n❌ Error al crear la instancia:")
            for error in operation.error.errors:
                print(f"  - {error.code}: {error.message}")
            return False
        else:
            print(f"\n✅ Instancia '{instance_name}' creada exitosamente!")
            print(f"   Zona: {zone}")
            print(f"   Tipo: {machine_type}")
            if ssh_key:
                print(f"   SSH: configurado")

            # Obtener la IP pública de la instancia creada
            print("\nObteniendo la IP pública de la máquina...")

            # Busca la instancia recién creada para obtener la IP
            instance_info = instance_client.get(
                project=project_id,
                zone=zone,
                instance=instance_name
            )
            public_ip = None
            for iface in instance_info.network_interfaces:
                if iface.access_configs:
                    for ac in iface.access_configs:
                        if ac.nat_i_p:
                            public_ip = ac.nat_i_p

            if public_ip:
                print(f"   IP pública: {public_ip}")
            else:
                print("   No se pudo obtener la IP pública de la instancia.")

            return True

    except Exception as e:
        print(f"\n❌ Error al crear la instancia: {e}")
        return False