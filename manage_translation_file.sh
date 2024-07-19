#!/bin/bash

# Nombre del archivo Python que contiene la lógica
PYTHON_SCRIPT="utils/translations/manage_translations.py"

# Verifica si se ha pasado un parámetro
if [ "$#" -eq 1 ]; then
    SPECIFIC_FILE="$1"
    python3 "$PYTHON_SCRIPT" "$SPECIFIC_FILE"
else
    python3 "$PYTHON_SCRIPT"
fi
