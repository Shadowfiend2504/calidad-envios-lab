import os
import sys

# Añadir la carpeta raíz del proyecto al sys.path para que pytest pueda importar `src`
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
