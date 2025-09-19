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
    raise NotImplementedError("Implementa calcular_costo_envio usando TDD")
