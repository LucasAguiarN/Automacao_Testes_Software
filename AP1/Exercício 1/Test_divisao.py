import unittest
import divisao

class TestDivisao(unittest.TestCase):
    def test_divisao_por_numero_inteiro(self):
        self.assertEqual(divisao.divisao(10, 2), 5)

    def test_divisao_por_numero_float(self):
        self.assertEqual(divisao.divisao(10, 2.5), 4)

    def test_divisao_por_zero(self):
        self.assertRaises(ValueError, divisao.divisao, 10, 0)

    def test_divisao_por_numero_invalido_input_1(self):
        self.assertRaises(TypeError, divisao.divisao, "10", 2)

    def test_divisao_por_numero_invalido_input_2(self):
        self.assertRaises(TypeError, divisao.divisao, 10, "2")

if __name__ == '__main__':
    unittest.main()