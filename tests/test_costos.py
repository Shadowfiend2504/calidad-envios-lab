import pytest

from src.costos import calcular_costo_envio

# Criterios de aceptación (implementados en las pruebas):
# CA1: Base 5000, recargo por peso según tramos, recargos multiplicativos
# CA2: Destino sólo 'nacional' o 'internacional'
# CA3: Prioridad sólo 'estandar' o 'express'
# CA4: Errores para peso <= 0 o inputs no válidos


@pytest.mark.parametrize(
    "peso,destino,prioridad,esperado",
    [
        # Partición: peso en (0,5]
        (1, "nacional", "estandar", 5000 + 2000 * 1),
        (5, "nacional", "estandar", 5000 + 2000 * 5),
        # Límite justo por encima de 5 -> cambia de tramo
        (5.0001, "nacional", "estandar", round(5000 + 1500 * 5.0001)),

        # Partición: (5,20]
        (10, "nacional", "estandar", 5000 + 1500 * 10),
        (20, "nacional", "estandar", 5000 + 1500 * 20),

        # Partición: > 20
        (20.1, "nacional", "estandar", round(5000 + 1200 * 20.1)),

        # Internacional aplica +25%
        (2, "internacional", "estandar", round((5000 + 2000 * 2) * 1.25)),

        # Express aplica +15%
        (2, "nacional", "express", round((5000 + 2000 * 2) * 1.15)),

        # Ambos recargos multiplicativos
        (2, "internacional", "express", round((5000 + 2000 * 2) * 1.25 * 1.15)),
    ],
)
def test_casos_validos(peso, destino, prioridad, esperado):
    resultado = calcular_costo_envio(peso, destino, prioridad)
    # comparar enteros
    assert int(resultado) == int(round(esperado))


@pytest.mark.parametrize(
    "peso,destino,prioridad",
    [
        # inválidos por peso
        (0, "nacional", "estandar"),
        (-1, "nacional", "estandar"),
        # destino inválido
        (3, "exterior", "estandar"),
        # prioridad inválida
        (3, "nacional", "rapida"),
        # tipo de peso no convertible
        ("dos", "nacional", "estandar"),
        (None, "nacional", "estandar"),
    ],
)
def test_casos_invalidos(peso, destino, prioridad):
    with pytest.raises(ValueError):
        calcular_costo_envio(peso, destino, prioridad)


def test_destino_y_prioridad_case_insensitive():
    # la función acepta mayúsculas/minúsculas en destino y prioridad
    assert (
        calcular_costo_envio(1, "NACIONAL", "ESTANDAR")
        == calcular_costo_envio(1, "nacional", "estandar")
    )
    assert (
        calcular_costo_envio(1, "Internacional", "Express")
        == calcular_costo_envio(1, "internacional", "express")
    )


def test_redondeo_al_entero_mas_cercano():
    # comprobar que el redondeo final es al entero más cercano
    val = calcular_costo_envio(5.5, "nacional", "estandar")
    # cálculo manual
    esperado = round(5000 + 5.5 * 1500)
    assert int(val) == int(esperado)


# (Opcional) propiedad: costo no disminuye al aumentar peso.
# Marca: property (puedes ejecutar: pytest -m "not property" para omitirla).
@pytest.mark.property
def test_monotonia_con_peso():
    # Hypothesis es opcional; si no está instalado omitimos esta prueba.
    pytest.importorskip("hypothesis")
    from hypothesis import given
    from hypothesis import strategies as st


    @given(
        st.floats(min_value=0.1, max_value=50),
        st.floats(min_value=0.1, max_value=50),
        st.sampled_from(["nacional", "internacional"]),
        st.sampled_from(["estandar", "express"]),
    )
    def prop(w1, w2, dest, pri):
        c1 = calcular_costo_envio(w1, dest, pri)
        c2 = calcular_costo_envio(w2, dest, pri)
        if w2 >= w1:
            assert c2 >= c1

    prop()
