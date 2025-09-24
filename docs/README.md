# Mini-laboratorio: Calculadora de envío con TDD + calidad

**Duración:** 1–2 horas  
**Objetivo:** Implementar y asegurar la calidad de una función `calcular_costo_envio(peso, destino, prioridad)` usando TDD, partición de equivalencia, valores límite, cobertura, estilo y complejidad.

## Reglas de negocio
- Base: **$5.000**
- Por peso:
  - 0 < peso ≤ 5 kg → + **$2.000/kg**
  - 5 < peso ≤ 20 kg → + **$1.500/kg**
  - peso > 20 kg → + **$1.200/kg**
- Destino:
  - `"nacional"` → **sin recargo**
  - `"internacional"` → **+25%** sobre el subtotal
- Prioridad:
  - `"estandar"` → **sin recargo**
  - `"express"` → **+15%** sobre el subtotal
- Redondeo al **entero más cercano** al final.
- Errores:
  - `peso ≤ 0` o no numérico → `ValueError`
  - `destino` no es `"nacional"`/`"internacional"` → `ValueError`
  - `prioridad` no es `"estandar"`/`"express"` → `ValueError`

## Actividades
1. Completa la tabla de Partición de Equivalencia (PE) y Análisis de Valores Límite (AVL) con al menos 8 casos válidos y 4 inválidos.
2. Ejecuta los tests (fallarán la primera vez): `pytest -q`.
3. Implementa `src/costos.py` hasta pasar todos los tests.
4. Mide y mejora calidad:
   - **Cobertura:** `coverage run -m pytest && coverage report -m` (objetivo ≥ 90%)
   - **Estilo:** `ruff check .` (0 errores)
   - **Complejidad:** `radon cc -s -a src` (media ≤ 5)
5. (Opcional) Valida propiedad de **monotonía** con `hypothesis`.

## Requisitos
- Python 3.10 o superior
- Crear y activar entorno virtual

### Setup rápido
```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest -q
```

## Estructura
```
calidad-envios-lab/
  ├─ src/
  │   └─ costos.py
  ├─ tests/
  │   └─ test_costos.py
  ├─ .coveragerc
  ├─ pyproject.toml
  ├─ requirements.txt
  └─ .github/workflows/python.yml
```

## Comandos útiles
```bash
pytest -q
coverage run -m pytest
coverage report -m
ruff check .
radon cc -s -a src
```

## Rúbrica sugerida (100 pts)
- 30 pts: Plan de pruebas (CA, PE/AVL bien justificado)
- 40 pts: Tests + cobertura ≥ 90% (incluye límites)
- 20 pts: Calidad estática (ruff ok) y complejidad (radon ≤ 5)
- 10 pts: Reporte claro (1 página) con evidencias y 3 defectos prevenidos

¡Éxitos y a probar primero! :)
