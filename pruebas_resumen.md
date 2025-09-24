# Resumen de Acciones Realizadas con Referencias

A continuación, se presenta un resumen estructurado de lo realizado, referenciando los apartados y fragmentos de código relevantes para facilitar el acceso:

---

## Implementación de la Función en `costos.py`

Implementé la función `calcular_costo_envio` respetando las reglas del enunciado: validaciones, cálculo por rangos de peso, recargos por destino y prioridad, y redondeo final.  
Ver: [Plan de pruebas, Casos válidos e inválidos](#plan-de-pruebas-ca-peavl--casos-sugeridos)

---

## Configuración del Entorno de Pruebas

Configuré el entorno virtual del proyecto e instalé `pytest`.  
Ver: [Cobertura y comandos recomendados](#cobertura-estilo-y-complejidad--comandos-recomendados)

---

## Ejecución de la Suite de Tests

Ejecuté la suite de tests existente:  
**Resultado actual:** 13 passed (todos los tests existentes pasan).
- **Evidencia (salida):**  
  ```
  13 passed in 2.38s
  ```
  Ver: [Ejecución de la Suite de Tests](#ejecución-de-la-suite-de-tests)

---

## Plan de Pruebas (Cobertura de Particiones y Límites)

Elaboré una tabla de Partición de Equivalencia (PE) y Análisis de Valores Límite (AVL) con casos concretos válidos e inválidos, para ser incorporada en el README como evidencia.  
Ver: [Plan de pruebas (CA, PE/AVL) — casos sugeridos](#plan-de-pruebas-ca-peavl--casos-sugeridos)

---

## Verificación de Cobertura y Calidad Estática

Aún no he medido la cobertura con `coverage` ni he ejecutado los chequeos de estilo (`ruff`) y complejidad (`radon`).  
**Siguiente acción recomendada:**
- Ejecutar cobertura y analizar los resultados.
- Ejecutar `ruff` para estilo.
- Ejecutar `radon` para complejidad.
Ver: [Cobertura y comandos recomendados](#cobertura-estilo-y-complejidad--comandos-recomendados)

---

## Reporte Final Pendiente

Falta redactar el reporte de 1 página incluyendo:
- Plan de pruebas (tabla PE/AVL)
- Evidencia de tests (salida pytest)
- Cobertura (tras medirla)
- Salidas de `ruff` y `radon`
- Tres defectos prevenidos (identificados a partir de los tests y validaciones implementadas)

Ver: [Reporte Final Pendiente](#reporte-final-pendiente)

---

## Mapeo a la Rúbrica (Estado por Ítem)

- Plan de pruebas (CA, PE/AVL bien justificado): Parcialmente hecho, tabla PE/AVL propuesta y casos sugeridos ([Ver tabla](#plan-de-pruebas-ca-peavl--casos-sugeridos))
- Tests + cobertura ≥ 90%: Tests ejecutados, falta medir cobertura ([Ver comandos](#cobertura-estilo-y-complejidad--comandos-recomendados))
- Calidad estática (ruff ok) y complejidad (radon ≤ 5): No ejecutado aún, instrucciones listadas ([Ver comandos](#cobertura-estilo-y-complejidad--comandos-recomendados))
- Reporte claro (1 página): Pendiente de elaboración ([Ver pendiente](#reporte-final-pendiente))

---

## Plan de pruebas (CA, PE/AVL) — Casos Sugeridos

**Objetivo:** cubrir particiones y límites. Incluyo 8 casos válidos y 4 inválidos.

### Casos válidos (8)

1. **CA1 — Peso pequeño, nacional, estandar (peso límite inferior dentro del rango 0 < p <= 5)**
   ```python
   # Entrada:
   calcular_costo_envio(peso=1.0, destino='nacional', prioridad='estandar')
   # Resultado esperado:
   # base 5000 + 2000*1 = 7000 → redondeo 7000
   ```
2. **CA2 — Peso en límite 5 kg, nacional, estandar (AVL)**
   ```python
   calcular_costo_envio(peso=5.0, destino='nacional', prioridad='estandar')
   # Esperado: 5000 + 2000*5 = 15000
   ```
3. **CA3 — Peso 6 kg (rango 5 < p <= 20), nacional, estandar**
   ```python
   calcular_costo_envio(peso=6.0, destino='nacional', prioridad='estandar')
   # Esperado: 5000 + 1500*6 = 14000
   ```
4. **CA4 — Peso 20 kg (límite) nacional, estandar (AVL)**
   ```python
   calcular_costo_envio(peso=20.0, destino='nacional', prioridad='estandar')
   # Esperado: 5000 + 1500*20 = 35000
   ```
5. **CA5 — Peso 21 kg (>20), nacional, estandar**
   ```python
   calcular_costo_envio(peso=21.0, destino='nacional', prioridad='estandar')
   # Esperado: 5000 + 1200*21 = 30200
   ```
6. **CA6 — Internacional, impacto del 25% (verificar multiplicación)**
   ```python
   calcular_costo_envio(peso=10.0, destino='internacional', prioridad='estandar')
   # Subtotal: 5000 + 1500*10 = 20000 → *1.25 = 25000
   ```
7. **CA7 — Express, impacto del 15% (verificar multiplicación)**
   ```python
   calcular_costo_envio(peso=10.0, destino='nacional', prioridad='express')
   # Subtotal: 20000 → *1.15 = 23000
   ```
8. **CA8 — Internacional + Express (combinación multiplicativa)**
   ```python
   calcular_costo_envio(peso=2.5, destino='internacional', prioridad='express')
   # Subtotal: 5000 + 2000*2.5 = 10000 → *1.25 = 12500 → *1.15 = 14375 → redondeo 14375
   ```

### Casos inválidos (4)

1. **INV1 — Peso 0 (error)**
   ```python
   calcular_costo_envio(peso=0, destino='nacional', prioridad='estandar')
   # Esperado: ValueError
   ```
2. **INV2 — Peso negativo (error)**
   ```python
   calcular_costo_envio(peso=-1, destino='nacional', prioridad='estandar')
   # Esperado: ValueError
   ```
3. **INV3 — Destino inválido (error)**
   ```python
   calcular_costo_envio(peso=1, destino='interplanetario', prioridad='estandar')
   # Esperado: ValueError
   ```
4. **INV4 — Prioridad inválida (error)**
   ```python
   calcular_costo_envio(peso=1, destino='nacional', prioridad='urgente')
   # Esperado: ValueError
   ```

> _Estos casos deben estar representados en los tests unitarios y agregarse si faltan en `test_costos.py`._

---

## Cobertura, Estilo y Complejidad — Comandos Recomendados

- **Ejecutar tests:**  
  ```sh
  .venv\Scripts\Activate.ps1
  python -m pytest -q
  ```

- **Medir cobertura:**
  ```sh
  python -m pip install coverage
  python -m coverage run -m pytest
  python -m coverage report -m
  ```

- **Estilo y complejidad:**
  ```sh
  python -m pip install ruff radon
  ruff check .
  radon cc -s -a src
  ```

- **Interpretación:**
  - `coverage report -m` debe mostrar un porcentaje total ≥ 90% (si no, añadir tests).
  - `ruff check .` → 0 errores (si hay errores, se corrigen).
  - `radon cc -s -a src` → "Average complexity" media ≤ 5 (si es mayor, refactorizar funciones de alto CC).

---

## Para consultar detalles, utiliza los accesos directos de código en cada apartado.
