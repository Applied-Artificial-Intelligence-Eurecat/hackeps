import argparse
import json
import os
from find_instance import find_instances
from create_instance import create_instance
from list_instances import list_instances
from delete_instance import delete_instance, find_and_delete_instance



def load_credentials(credentials_file):
    """Carga las credenciales desde un archivo JSON"""
    with open(credentials_file, 'r') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description='Gestionar instancias de GCP'
    )
    
    # Acciones
    parser.add_argument(
        '--find-instance',
        action='store_true',
        help='Buscar instancias compatibles'
    )
    
    parser.add_argument(
        '--create-instance',
        action='store_true',
        help='Crear una nueva instancia'
    )
    
    parser.add_argument(
        '--list-instances',
        action='store_true',
        help='Listar todas las instancias del proyecto'
    )
    
    parser.add_argument(
        '--delete-instance',
        action='store_true',
        help='Borrar una instancia del proyecto'
    )
    
    # Parámetros comunes
    parser.add_argument(
        '--credentials',
        required=True,
        help='Ruta al archivo de credenciales de GCP (JSON)'
    )
    
    parser.add_argument(
        '--zone',
        help='Zona de GCP (ej: us-central1-a) - requerido para --find-instance y --create-instance'
    )
    
    # Parámetros para find-instance
    parser.add_argument(
        '--region',
        help='Región de GCP (ej: us-central1) - requerido para --find-instance'
    )
    
    parser.add_argument(
        '--cpus',
        type=int,
        help='Número mínimo de CPUs - requerido para --find-instance'
    )
    
    parser.add_argument(
        '--ram',
        type=int,
        help='Cantidad mínima de RAM en GB - requerido para --find-instance'
    )
    
    
    parser.add_argument(
        '--machine-type',
        help='Tipo de máquina (ej: e2-medium, n1-standard-1) - requerido para --create-instance'
    )
    
    parser.add_argument(
        '--ssh-key',
        help='Clave SSH pública para acceso a la instancia (formato: usuario:ssh-rsa AAAA...)'
    )
    
    parser.add_argument(
        '--name',
        help='Nombre de la instancia (ej: node1, node2, node3, etc.)'
    )
    
    args = parser.parse_args()
    
    # Validar que se haya seleccionado una acción
    if not args.find_instance and not args.create_instance and not args.list_instances and not args.delete_instance:
        parser.print_help()
        return
    
    # Cargar credenciales
    print(f"Cargando credenciales desde: {args.credentials}")
    credentials = load_credentials(args.credentials)
    
    # Configurar variable de entorno para autenticación
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = args.credentials
    
    if args.find_instance:
        # Validar parámetros requeridos para find-instance
        if not all([args.region, args.cpus, args.ram, args.zone]):
            parser.error("--find-instance requiere --region, --cpus y --ram y --zone")
        
        # Buscar instancias
        find_instances(
            project_id=credentials['project_id'],
            zone=args.zone,
            region=args.region,
            num_cpus=args.cpus,
            num_ram_gb=args.ram
        )
    
    elif args.create_instance:
        # Validar parámetros requeridos para create-instance
        if not all([args.name, args.machine_type, args.zone]):
            parser.error("--create-instance requiere --name, --machine-type, --zone")
        
        
        # Crear instancia
        create_instance(
            project_id=credentials['project_id'],
            zone=args.zone,
            instance_name=args.name,
            machine_type=args.machine_type,
            ssh_key=args.ssh_key
        )
    
    elif args.list_instances:
        # Listar instancias
        list_instances(
            project_id=credentials['project_id'],
            zone=args.zone,
        )
    
    elif args.delete_instance:
        # Validar parámetros requeridos para delete-instance
        if not args.name:
            parser.error("--delete-instance requiere --name")
        
        # Borrar instancia
        if args.zone:
            # Borrar en una zona específica
            delete_instance(
                project_id=credentials['project_id'],
                zone=args.zone,
                instance_name=args.name
            )
        else:
            # Buscar en todas las zonas y borrar
            find_and_delete_instance(
                project_id=credentials['project_id'],
                instance_name=args.name
            )


if __name__ == '__main__':
    main()
