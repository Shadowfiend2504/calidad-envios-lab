import pytest
from src.costos import calcular_costo_envio

@pytest.mark.parametrize(
    "peso,destino,prioridad,esperado",
    [
        (1,    "nacional",      "estandar", 7000),
        (5,    "nacional",      "estandar", 15000),
        (5.01, "nacional",      "estandar", round(5000 + 5.01*1500)),
        (20,   "nacional",      "estandar", 35000),
        (20.1, "nacional",      "estandar", round(5000 + 20.1*1200)),
        (2,    "internacional", "estandar", round((5000 + 2*2000) * 1.25)),
        (2,    "nacional",      "express",  round((5000 + 2*2000) * 1.15)),
        (2,    "internacional", "express",  round((5000 + 2*2000) * 1.25 * 1.15)),
    ],
)
def test_casos_validos(peso, destino, prioridad, esperado):
    assert calcular_costo_envio(peso, destino, prioridad) == esperado

@pytest.mark.parametrize(
    "peso,destino,prioridad",
    [
        (0, "nacional", "estandar"),
        (-1, "nacional", "estandar"),
        (3, "exterior", "estandar"),
        (3, "nacional", "rapida"),
    ],
)
def test_casos_invalidos(peso, destino, prioridad):
    with pytest.raises(ValueError):
        calcular_costo_envio(peso, destino, prioridad)

# (Opcional) propiedad: costo no disminuye al aumentar peso.
# Marca: property (puedes ejecutar: pytest -m "not property" para omitirla).
@pytest.mark.property
def test_monotonia_con_peso():
    from hypothesis import given, strategies as st
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
