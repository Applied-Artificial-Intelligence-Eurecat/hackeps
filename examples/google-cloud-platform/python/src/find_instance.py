#!/usr/bin/env python3
"""
Script simple para buscar instancias de GCP según criterios
"""
import argparse
import json
from google.cloud import compute_v1


def find_instances(project_id, zone, region, num_cpus, num_ram_gb):
    """
    Busca tipos de instancias que cumplan con los requisitos
    
    Args:
        project_id: ID del proyecto de GCP
        zone: Zona de GCP (ej: us-central1-a)
        region: Región de GCP (ej: us-central1)
        num_cpus: Número mínimo de CPUs
        num_ram_gb: Cantidad mínima de RAM en GB
    """
    print(f"Buscando instancias en zona: {zone}")
    print(f"Requisitos: {num_cpus} CPUs, {num_ram_gb} GB RAM")
    
    # Cliente de compute
    client = compute_v1.MachineTypesClient()
    
    # Lista de tipos de máquina disponibles
    machine_types = []
    
    try:
        # Obtener tipos de máquina en la zona especificada
        request = compute_v1.ListMachineTypesRequest(
            project=project_id,
            zone=zone
        )
        
        for machine_type in client.list(request=request):
            # Convertir MB a GB para la RAM
            ram_gb = machine_type.memory_mb / 1024
            
            # Filtrar por requisitos
            if machine_type.guest_cpus == num_cpus and ram_gb == num_ram_gb :
                machine_types.append({
                    'name': machine_type.name,
                    'cpus': machine_type.guest_cpus,
                    'ram_gb': round(ram_gb, 2),
                    'description': machine_type.description
                })
        
        # Mostrar resultados
        print(f"\nEncontradas {len(machine_types)} instancias compatibles:\n")
        for mt in machine_types[:10]:  # Mostrar solo las primeras 10
            print(f"  - {mt['name']}: {mt['cpus']} CPUs, {mt['ram_gb']} GB RAM")
            print(f"    {mt['description']}")
            print()
        
        if len(machine_types) > 10:
            print(f"... y {len(machine_types) - 10} más")
        
        return machine_types
        
    except Exception as e:
        print(f"Error al buscar instancias: {e}")
        return []

