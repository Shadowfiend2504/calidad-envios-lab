# TODO: Implementa la función siguiendo TDD.
# Recomendación: corre primero los tests para verlos fallar.
# Luego implementa y mantén el código simple.

def calcular_costo_envio(peso: float, destino: str, prioridad: str) -> int:
    """Calcula el costo de envío según reglas de negocio.

    Reglas:
    - Base: 5000
    - Por peso:
        0 < peso <= 5      -> + 2000 * peso
        5 < peso <= 20     -> + 1500 * peso
        peso > 20          -> + 1200 * peso
    - Destino:
        'nacional'         -> sin recargo
        'internacional'    -> +25% sobre el subtotal
    - Prioridad:
        'estandar'         -> sin recargo
        'express'          -> +15% sobre el subtotal
    - Redondeo al entero más cercano al final.

    Validaciones:
    - peso <= 0 o no numérico -> ValueError
    - destino no válido -> ValueError
    - prioridad no válida -> ValueError
    """
    # Validaciones
    try:
        peso_val = float(peso)
    except Exception:
        raise ValueError("peso debe ser un número mayor que 0")

    if peso_val <= 0:
        raise ValueError("peso debe ser un número mayor que 0")

    destino = destino.lower() if isinstance(destino, str) else destino
    prioridad = prioridad.lower() if isinstance(prioridad, str) else prioridad

    if destino not in ("nacional", "internacional"):
        raise ValueError("destino no válido")

    if prioridad not in ("estandar", "express"):
        raise ValueError("prioridad no válida")

    # Base
    subtotal = 5000.0

    # Costo por peso
    if 0 < peso_val <= 5:
        subtotal += 2000.0 * peso_val
    elif 5 < peso_val <= 20:
        subtotal += 1500.0 * peso_val
    else:  # peso_val > 20
        subtotal += 1200.0 * peso_val

    # Recargo por destino
    if destino == "internacional":
        subtotal *= 1.25

    # Recargo por prioridad
    if prioridad == "express":
        subtotal *= 1.15

    # Redondeo al entero más cercano
    return int(round(subtotal))
