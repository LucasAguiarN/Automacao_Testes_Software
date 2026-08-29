import pytest
from medico import calcular_dosagem

def test_calcular_dosagem_ValueError_1():
    with pytest.raises(ValueError):
        calcular_dosagem(-1, 5)

def test_calcular_dosagem_ValueError_2():
    with pytest.raises(ValueError):
        calcular_dosagem(250, 5)

def test_calcular_dosagem_ValueError_3():
    with pytest.raises(ValueError):
        calcular_dosagem(1, -1)

def test_calcular_dosagem_ValueError_4():
    with pytest.raises(ValueError):
        calcular_dosagem(1, 250)

def test_calcular_dosagem_1():
    assert calcular_dosagem(20, 60) == 1000

def test_calcular_dosagem_2():
    assert calcular_dosagem(12, 60) == 1000

def test_calcular_dosagem_3():
    assert calcular_dosagem(20, 59) == 875

def test_calcular_dosagem_4():
    assert calcular_dosagem(12, 59) == 875

def test_calcular_dosagem_5():
    assert calcular_dosagem(1, 5) == 125

def test_calcular_dosagem_6():
    assert calcular_dosagem(1, 9) == 125

def test_calcular_dosagem_7():
    assert calcular_dosagem(2, 9.1) == 250

def test_calcular_dosagem_8():
    assert calcular_dosagem(2, 16) == 250

def test_calcular_dosagem_9():
    assert calcular_dosagem(3, 16.1) == 375

def test_calcular_dosagem_10():
    assert calcular_dosagem(3, 24) == 375

def test_calcular_dosagem_11():
    assert calcular_dosagem(4, 24.1) == 500

def test_calcular_dosagem_12():
    assert calcular_dosagem(5, 30) == 500

def test_calcular_dosagem_13():
    assert calcular_dosagem(6, 30.1) == 750