# Scripts de GCP - Guía Rápida

## Requisitos previos

- Python 3.8 o superior
- Credenciales de servicio de GCP (archivo JSON)

## Preparación

### 1. Entorno
```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows:
env\Scripts\activate
# En Linux/Mac:
source env/bin/activate

# Instalamos las dependencias
pip install -r requirements.txt
```

### 2. Configurar credenciales

1. Solicita tus credenciales de equipo (un archivo .json)
2. Guárdalo en alguna ruta que puedas localizar

### 3. Creación de clave SSH
```bash
ssh-keygen -t rsa -b 4096 -C "username"
```

Este comando os dará dos archivos:
- La clave privada, que no tiene extensión
- La clave pública, que termina en .pub

## Uso

### 1. Crear instancia
```bash
python src/main.py --create-instance --credentials ..\google-cloud-credentials.json --region europe-west1-b --zone europe-west1-b --machine-type c4-highcpu-2 --name test --ssh-key "username:la_clave_ssh_publica"
```

**Parámetros:**
- `--credentials`: Ruta al archivo de credenciales JSON
- `--region`: Región de GCP (ej: europe-west1)
- `--zone`: Zona de GCP (ej: europe-west1-b)
- `--machine-type`: Tipo de máquina (ej: c4-highcpu-2, e2-medium)
- `--name`: Nombre de la instancia
- `--ssh-key`: Clave SSH pública en formato "usuario:clave_publica"

### 2. Listar instancias
```bash
# Listar todas las instancias en una zona
python src/main.py --list-instances --credentials ..\google-cloud-credentials.json --zone europe-west1-b

# Listar todas las instancias en todas las zonas
python src/main.py --list-instances --credentials ..\google-cloud-credentials.json
```

### 3. Borrar instancia

```bash
# Borrar instancia especificando la zona
python src/main.py --delete-instance --credentials ..\google-cloud-credentials.json --name test --zone europe-west1-b

# Borrar instancia buscando en todas las zonas
python src/main.py --delete-instance --credentials ..\google-cloud-credentials.json --name test
```

**Nota:** Si no especificas la zona, el script buscará la instancia en todas las zonas disponibles.

### 4. Buscar tipos de instancia
```bash
python src/main.py --find-instance --credentials ..\google-cloud-credentials.json --zone europe-west1-b --region europe-west1 --cpus 2 --ram 4
```

**Parámetros:**
- `--cpus`: Número mínimo de CPUs requeridas
- `--ram`: Cantidad mínima de RAM en GB

Este comando te ayudará a encontrar tipos de máquinas que cumplan con tus requisitos de CPU y RAM.
