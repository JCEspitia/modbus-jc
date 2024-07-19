#!/bin/bash

# Nombre del archivo Python que contiene la lógica
PYTHON_SCRIPT="utils/ui_files_manager/ui_files_manager.py"

# Verifica si se ha pasado un parámetro
if [ "$#" -eq 1 ]; then
    SPECIFIC_FILE="$1"
    python3 "$PYTHON_SCRIPT" "$SPECIFIC_FILE"
else
    python3 "$PYTHON_SCRIPT"
fi
