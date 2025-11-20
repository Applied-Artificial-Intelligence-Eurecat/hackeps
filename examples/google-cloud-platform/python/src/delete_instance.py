#!/usr/bin/env python3
"""
Script para borrar una instancia de GCP por su nombre
"""
import argparse
import json
from google.cloud import compute_v1


def delete_instance(project_id, zone, instance_name):
    """
    Borra una instancia de GCP
    
    Args:
        project_id: ID del proyecto de GCP
        zone: Zona de GCP donde está la instancia
        instance_name: Nombre de la instancia a borrar
    
    Returns:
        bool: True si se borró exitosamente, False en caso contrario
    """
    instance_client = compute_v1.InstancesClient()
    
    try:
        # Primero verificar si la instancia existe
        print(f"Verificando si la instancia '{instance_name}' existe en la zona {zone}...")
        
        try:
            instance = instance_client.get(
                project=project_id,
                zone=zone,
                instance=instance_name
            )
            print(f"✓ Instancia encontrada: {instance.name}")
            print(f"  Estado: {instance.status}")
            print(f"  Tipo: {instance.machine_type.split('/')[-1]}")
            print()
        except Exception as e:
            print(f"❌ Error: La instancia '{instance_name}' no existe en la zona {zone}")
            return False
        
        # Confirmar borrado
        print(f"⚠️  ADVERTENCIA: Estás a punto de borrar la instancia '{instance_name}'")
        print(f"   Esta acción NO se puede deshacer.")
        print()
        
        # Proceder con el borrado
        print(f"Enviando solicitud de borrado...")
        
        request = compute_v1.DeleteInstanceRequest(
            project=project_id,
            zone=zone,
            instance=instance_name
        )
        
        operation = instance_client.delete(request=request)
        
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
            print(f"\n❌ Error al borrar la instancia:")
            for error in operation.error.errors:
                print(f"  - {error.code}: {error.message}")
            return False
        else:
            print(f"\n✅ Instancia '{instance_name}' borrada exitosamente!")
            print(f"   Zona: {zone}")
            return True
            
    except Exception as e:
        print(f"\n❌ Error al borrar la instancia: {e}")
        return False


def find_and_delete_instance(project_id, instance_name):
    """
    Busca una instancia en todas las zonas y la borra
    
    Args:
        project_id: ID del proyecto de GCP
        instance_name: Nombre de la instancia a borrar
    
    Returns:
        bool: True si se borró exitosamente, False en caso contrario
    """
    print(f"Buscando instancia '{instance_name}' en todas las zonas...\n")
    
    instance_client = compute_v1.InstancesClient()
    zones_client = compute_v1.ZonesClient()
    
    try:
        # Listar todas las zonas
        request = compute_v1.ListZonesRequest(project=project_id)
        zones = list(zones_client.list(request=request))
        
        # Buscar la instancia en cada zona
        for zone_info in zones:
            zone_name = zone_info.name
            try:
                instance = instance_client.get(
                    project=project_id,
                    zone=zone_name,
                    instance=instance_name
                )
                
                # Si llegamos aquí, la instancia existe en esta zona
                print(f"✓ Instancia encontrada en la zona: {zone_name}")
                print(f"  Estado: {instance.status}")
                print(f"  Tipo: {instance.machine_type.split('/')[-1]}")
                print()
                
                # Borrar la instancia
                return delete_instance(project_id, zone_name, instance_name)
                
            except Exception:
                # La instancia no está en esta zona, continuar buscando
                pass
        
        # Si llegamos aquí, no se encontró la instancia en ninguna zona
        print(f"❌ Error: La instancia '{instance_name}' no se encontró en ninguna zona del proyecto")
        return False
        
    except Exception as e:
        print(f"❌ Error al buscar la instancia: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Borrar una instancia de GCP'
    )
    
    parser.add_argument(
        '--credentials',
        required=True,
        help='Ruta al archivo de credenciales de GCP (JSON)'
    )
    
    parser.add_argument(
        '--name',
        required=True,
        help='Nombre de la instancia a borrar'
    )
    
    parser.add_argument(
        '--zone',
        help='Zona de GCP donde está la instancia (ej: us-central1-a). Si no se especifica, busca en todas las zonas'
    )
    
    args = parser.parse_args()
    
    # Cargar credenciales
    print(f"Cargando credenciales desde: {args.credentials}\n")
    
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = args.credentials
    
    with open(args.credentials, 'r') as f:
        credentials = json.load(f)
    
    # Borrar instancia
    if args.zone:
        # Borrar en una zona específica
        success = delete_instance(
            project_id=credentials['project_id'],
            zone=args.zone,
            instance_name=args.name
        )
    else:
        # Buscar en todas las zonas y borrar
        success = find_and_delete_instance(
            project_id=credentials['project_id'],
            instance_name=args.name
        )
    
    if success:
        print("\n🎉 Operación completada exitosamente")
    else:
        print("\n⚠️  La operación no se pudo completar")


if __name__ == '__main__':
    main()

