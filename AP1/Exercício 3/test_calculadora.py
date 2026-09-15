import pytest
from calculadora import calcular_valor_final


class TestCalculadoraDescontos:

    def test_compra_abaixo_100(self):
        assert calcular_valor_final(99.99) == 99.99

    def test_compra_exatamente_100(self):
        assert calcular_valor_final(100.00) == 100.00

    def test_compra_acima_100(self):
        assert calcular_valor_final(101.00) == 90.90

    def test_compra_exatamente_500(self):
        assert calcular_valor_final(500.00) == 450.00

    def test_compra_acima_500(self):
        assert calcular_valor_final(501.00) == 400.80

    def test_compra_com_valor_zero(self):
        with pytest.raises(ValueError):
            calcular_valor_final(0)

    def test_compra_com_valor_negativo(self):
        with pytest.raises(ValueError):
            calcular_valor_final(-1.00)