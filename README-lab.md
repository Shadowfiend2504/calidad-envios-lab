Mini-laboratorio: Calculadora de envío con TDD + calidad

Resumen

Este repositorio contiene una función `calcular_costo_envio(peso, destino, prioridad)` con pruebas basadas en TDD y herramientas de calidad.

Cómo ejecutar (Windows PowerShell)

1. Crear entorno virtual e instalar dependencias:

```powershell
cd C:\GitHub\Codigos\calidad-envios-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Ejecutar tests:

```powershell
pytest -q
```

3. Ejecutar cobertura:

```powershell
coverage run -m pytest && coverage report -m
```

4. Ejecutar ruff:

```powershell
ruff check .
```

5. Medir complejidad con radon:

```powershell
radon cc -s src
```

Notas

- Las pruebas de propiedad con hypothesis están marcadas con `@pytest.mark.property`. Puedes omitirlas con `pytest -m "not property"` si no quieres ejecutarlas.
