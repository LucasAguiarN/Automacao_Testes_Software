import pytest
from calculadora_peso import obter_peso_ideal

def test_1_obter_peso_ideal():
    assert obter_peso_ideal(1.5, 'M') == pytest.approx(51.05, 0.01)

def test_2_obter_peso_ideal():
    assert obter_peso_ideal(1.5, 'F') == pytest.approx(48.45, 0.01)

def test_3_obter_peso_ideal():
    assert obter_peso_ideal(1.6, 'M') == pytest.approx(58.32, 0.01)

def test_4_obter_peso_ideal():
    assert obter_peso_ideal(1.6, 'F') == pytest.approx(54.66, 0.01)

def test_5_obter_peso_ideal():
    assert obter_peso_ideal(1.7, 'M') == pytest.approx(65.59, 0.01)

def test_6_obter_peso_ideal():
    assert obter_peso_ideal(1.7, 'F') == pytest.approx(60.86, 0.01)

def test_7_obter_peso_ideal():
    assert obter_peso_ideal(1.8, 'M') == pytest.approx(72.86, 0.01)

def test_8_obter_peso_ideal():
    assert obter_peso_ideal(1.8, 'F') == pytest.approx(67.08, 0.01)

def test_9_obter_peso_ideal():
    assert obter_peso_ideal(1.9, 'M') == pytest.approx(80.13, 0.01)

def test_10_obter_peso_ideal():
    assert obter_peso_ideal(1.9, 'F') == pytest.approx(73.28, 0.01)

def test_11_obter_peso_ideal():
    assert obter_peso_ideal(2.0, 'M') == pytest.approx(87.4, 0.01)

def test_12_obter_peso_ideal():
    assert obter_peso_ideal(2.0, 'F') == pytest.approx(79.5, 0.01)