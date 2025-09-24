# Criterios de aceptación (CA) y particiones para `calcular_costo_envio`

## Criterios de aceptación (CA)

- CA1: La función debe devolver un entero con el costo total redondeado al entero más cercano.
- CA2: Base fija de 5000.
- CA3: Recargo por peso:
  - 0 < peso <= 5: 2000 * peso
  - 5 < peso <= 20: 1500 * peso
  - peso > 20: 1200 * peso
- CA4: Destino puede ser 'nacional' (sin recargo) o 'internacional' (+25% sobre subtotal).
- CA5: Prioridad puede ser 'estandar' (sin recargo) o 'express' (+15% sobre subtotal).
- CA6: Si input inválido -> ValueError.

## Particiones de equivalencia (PE)

- PE1: Peso inválido (<= 0, no numérico)
- PE2: Peso en (0, 5]
- PE3: Peso en (5, 20]
- PE4: Peso > 20
- PE5: Destino inválido
- PE6: Prioridad inválida

## Análisis de valores límite (AVL)

- Límites en 0, 5, 20. Probar justo por debajo, igual y justo por encima cuando corresponda.


## Notas

Las pruebas en `tests/test_costos.py` implementan estas particiones y límites, y además incluyen una prueba de propiedad opcional con `hypothesis` que verifica monotonicidad con respecto al peso.
