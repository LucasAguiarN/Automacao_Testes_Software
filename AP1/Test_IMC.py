import pytest
from IMC import calcular_imc

def test_calcular_imc_TypeError():
    with pytest.raises(TypeError):
        calcular_imc("Lucas", "70", 1.59)

def test_abaixo_peso():
    assert calcular_imc("Lucas", 18.49, 1.0) == "Lucas seu IMC é Abaixo do Peso"

def test_peso_normal_limite_inferior():
    assert calcular_imc("Lucas", 18.5, 1.0) == "Lucas seu IMC é Peso Normal"

def test_peso_normal_limite_superior():
    assert calcular_imc("Lucas", 24.9, 1.0) == "Lucas seu IMC é Peso Normal"

def test_sobrepeso_limite_inferior():
    assert calcular_imc("Lucas", 25.0, 1.0) == "Lucas seu IMC é Sobrepeso"

def test_sobrepeso_limite_superior():
    assert calcular_imc("Lucas", 29.9, 1.0) == "Lucas seu IMC é Sobrepeso"

def test_obesidade_grau_I_limite_inferior():
    assert calcular_imc("Lucas", 30.0, 1.0) == "Lucas seu IMC é Obesidade Grau I"

def test_obesidade_grau_I_limite_superior():
    assert calcular_imc("Lucas", 34.9, 1.0) == "Lucas seu IMC é Obesidade Grau I"

def test_obesidade_grau_II_limite_inferior():
    assert calcular_imc("Lucas", 35.0, 1.0) == "Lucas seu IMC é Obesidade Grau II"

def test_obesidade_grau_II_limite_superior():
    assert calcular_imc("Lucas", 39.9, 1.0) == "Lucas seu IMC é Obesidade Grau II"

def test_obesidade_grau_III():
    assert calcular_imc("Lucas", 40.0, 1.0) == "Lucas seu IMC é Obesidade Grau III"