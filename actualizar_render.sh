#!/bin/bash

# Activar el entorno virtual
source /opt/render/project/src/.venv/bin/activate

# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias desde requirements.txt
pip install -r /opt/render/project/src/requirements.txt
