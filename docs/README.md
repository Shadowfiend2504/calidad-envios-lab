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

Se ejecutaron las comprobaciones locales de cobertura, estilo y complejidad. Resumen de resultados:

- Coverage: 100% en `src/costos.py` (ejecutado con `coverage run -m pytest` y `coverage report -m`).
- Ruff: se ejecutó `ruff check .`; detectó problemas menores en los tests — la mayoría se corrigieron con `ruff check . --fix`.
- Radon: `radon cc -s src` reportó complejidad ciclomática elevada para `calcular_costo_envio` (nivel C, valor 11). Se recomienda refactorizar si se desea reducir la complejidad por debajo de 5.

> Detalles y comandos para replicar están en `Ejercicio.md` (sección "Comandos utiles").

---
# Resumen mínimo de pruebas

Acciones clave:

- Implementada `calcular_costo_envio` con validaciones, tramos por peso, recargos y redondeo.
- Tests unitarios: casos válidos, casos inválidos y pruebas de límites (PE + AVL).
- Se recomienda ejecutar coverage, ruff y radon para verificar calidad y complejidad.

## Casos de prueba (resumen)

- Válidos: peso 1 (0<p<=5), peso 5 (límite), peso 6 (5<p<=20), peso 20 (límite), peso 21 (>20), internacional, express, internacional+express.
- Inválidos: peso 0, peso negativo, destino inválido, prioridad inválida.
## Cómo encajan en un flujo TDD + calidad

- PE + AVL: diseñar los tests unitarios (casos representativos + límites).
- TDD: escribir tests (PE/AVL) primero, luego implementar `calcular_costo_envio`.
- Ruff: mantener estilo y detectar problemas simples durante desarrollo.
- Radon: evaluar complejidad y decidir refactorizaciones para mejorar testabilidad.
- Hypothesis: añadir pruebas de propiedad para capturar casos inesperados automáticamente.
