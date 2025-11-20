#!/usr/bin/env python3
"""
Script para listar todas las instancias de GCP en un proyecto
"""
import argparse
import json
from google.cloud import compute_v1


def list_instances(project_id, zone=None):
    """
    Lista todas las instancias de GCP en el proyecto
    
    Args:
        project_id: ID del proyecto de GCP
        zone: Zona de GCP (opcional). Si no se especifica, lista instancias de todas las zonas
        team_name: Nombre del equipo para filtrar instancias (opcional). Solo muestra instancias que empiezan con este nombre
    """
    instance_client = compute_v1.InstancesClient()
    
    try:
        if zone:
            # Listar instancias en una zona específica
            print(f"Listando instancias en la zona: {zone}\n")
            
            request = compute_v1.ListInstancesRequest(
                project=project_id,
                zone=zone
            )
            
            instances = list(instance_client.list(request=request))
            
            # Filtrar por nombre de equipo si se especifica
            if not instances:
                print(f"No se encontraron instancias en la zona {zone}")
                return []
            
            print(f"Encontradas {len(instances)} instancia(s):\n")
            print_instances(instances, zone)
            
            return instances
        else:
            # Listar instancias en todas las zonas
            print("Listando instancias en todas las zonas...\n")
            
            zones_client = compute_v1.ZonesClient()
            
            request = compute_v1.ListZonesRequest(project=project_id)
            zones = list(zones_client.list(request=request))
            
            all_instances = []
            total_count = 0
            
            for zone_info in zones:
                zone_name = zone_info.name
                try:
                    request = compute_v1.ListInstancesRequest(
                        project=project_id,
                        zone=zone_name
                    )
                    instances = list(instance_client.list(request=request))
                    
                    # Filtrar por nombre de equipo si se especifica
                    if instances:
                        print(f"═══ Zona: {zone_name} ({len(instances)} instancia(s)) ═══")
                        print_instances(instances, zone_name)
                        print()
                        all_instances.extend(instances)
                        total_count += len(instances)
                except Exception as e:
                    # Algunas zonas pueden no estar disponibles
                    pass
            
            if total_count == 0:
                print("No se encontraron instancias en ninguna zona del proyecto")
            else:
                print(f"\n{'='*60}")
                print(f"TOTAL: {total_count} instancia(s) en el proyecto")
                print(f"{'='*60}")
            
            return all_instances
            
    except Exception as e:
        print(f"❌ Error al listar instancias: {e}")
        return []


def print_instances(instances, zone):
    """
    Imprime información detallada de las instancias
    
    Args:
        instances: Lista de instancias
        zone: Zona de las instancias
    """
    for instance in instances:
        status_emoji = "🟢" if instance.status == "RUNNING" else "🔴" if instance.status == "TERMINATED" else "🟡"
        
        print(f"{status_emoji} Nombre: {instance.name}")
        print(f"   Estado: {instance.status}")
        print(f"   Tipo de máquina: {instance.machine_type.split('/')[-1]}")
        print(f"   Zona: {zone}")
        
        # Obtener IPs
        if instance.network_interfaces:
            for iface in instance.network_interfaces:
                if iface.network_i_p:
                    print(f"   IP interna: {iface.network_i_p}")
                if iface.access_configs:
                    for ac in iface.access_configs:
                        if ac.nat_i_p:
                            print(f"   IP pública: {ac.nat_i_p}")
        
        # Obtener información de discos
        if instance.disks:
            disk_info = []
            for disk in instance.disks:
                if disk.boot:
                    disk_info.append("boot")
            if disk_info:
                print(f"   Discos: {', '.join(disk_info)}")
        
        # Fecha de creación
        if instance.creation_timestamp:
            print(f"   Creada: {instance.creation_timestamp}")
        
        print()


def main():
    parser = argparse.ArgumentParser(
        description='Listar instancias de GCP'
    )
    
    parser.add_argument(
        '--credentials',
        required=True,
        help='Ruta al archivo de credenciales de GCP (JSON)'
    )
    
    parser.add_argument(
        '--zone',
        help='Zona de GCP (ej: us-central1-a). Si no se especifica, lista todas las zonas'
    )
    
    parser.add_argument(
        '--team-name',
        help='Nombre del equipo para filtrar instancias (ej: team1, team2). Solo muestra instancias que empiezan con este nombre'
    )
    
    args = parser.parse_args()
    
    # Cargar credenciales
    print(f"Cargando credenciales desde: {args.credentials}\n")
    
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = args.credentials
    
    with open(args.credentials, 'r') as f:
        credentials = json.load(f)
    
    # Listar instancias
    list_instances(
        project_id=credentials['project_id'],
        zone=args.zone,
        team_name=args.team_name
    )


if __name__ == '__main__':
    main()

