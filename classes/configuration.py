# Nombre del usuario
USER="sps"

# User root
ROOT="root"

# Directorio del proyecto, "/" si es el directorio RAIZ
PROJECT_DIR="/examen"

# Directorio base del proyecto
BASE_DIR=f"/home/{USER}{PROJECT_DIR if PROJECT_DIR else '/'}"

# Dirección del archivo ON SH
ON_SH=f"{BASE_DIR}/scripts/sh/on.sh"

# Dirección del archivo OFF SH
OFF_SH=f"{BASE_DIR}/scripts/sh/off.sh"

# Dirección del archivo On C
ON_C=f"{BASE_DIR}/scripts/c/on"

# Dirección del archivo Off C
OFF_C=f"{BASE_DIR}/scripts/c/off"

# Dirección del archivo ON ASM
ON_ASM=f"{BASE_DIR}/scripts/asm/uthonremoto"

# Dirección del archivo OFF ASM
OFF_ASM=f"{BASE_DIR}/scripts/asm/uthoffremoto"

# Dirección del archivo OFF ASM-SH
ON_ASM_SH=f"{BASE_DIR}/scripts/asm/on"
OFF_ASM_SH=f"{BASE_DIR}/scripts/asm/off"


# Dirección de la imagen ON
ON_IMG=f"{BASE_DIR}/img/on.gif"

# Dirección de la imagen OFF
OFF_IMG=f"{BASE_DIR}/img/off.gif"

# Dirección del archivo status donde se guarda el estado del GPIO
STATUS=f"{BASE_DIR}/status/status.txt"

# Correo electrónico
EMAIL_SH=f"{BASE_DIR}/scripts/sh/read.sh"
