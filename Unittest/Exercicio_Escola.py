import unittest
import escolar

class TestEscola(unittest.TestCase):
    def test_avaliar_notas_valor_invalido_n1(self):
        self.assertRaisesRegex(ValueError, "Valor inválido para n1", escolar.avaliar_notas, -1, 0, 0, 0)

    def test_avaliar_notas_valor_invalido_n2(self):
        self.assertRaisesRegex(ValueError, "Valor inválido para n2", escolar.avaliar_notas, 0, -1, 0, 0)

    def test_avaliar_notas_valor_invalido_n3(self):
        self.assertRaisesRegex(ValueError, "Valor inválido para n3", escolar.avaliar_notas, 0, 0, -1, 0)

    def test_avaliar_notas_limite_A(self):
        self.assertEqual(escolar.avaliar_notas(10, 10, 10, 10), "A")

    def test_avaliar_notas_minimo_A(self):
        self.assertEqual(escolar.avaliar_notas(9, 9, 9, 9), "A")

    def test_avaliar_notas_limite_B(self):
        self.assertEqual(escolar.avaliar_notas(8.9, 8.9, 8.9, 8.9), "B")

    def test_avaliar_notas_minimo_B(self):
        self.assertEqual(escolar.avaliar_notas(7.5, 7.5, 7.5, 7.5), "B")

    def test_avaliar_notas_limite_C(self):
        self.assertEqual(escolar.avaliar_notas(7.4, 7.4, 7.4, 7.4), "C")

    def test_avaliar_notas_minimo_C(self):
        self.assertEqual(escolar.avaliar_notas(6.0, 6.0, 6.0, 6.0), "C")

    def test_avaliar_notas_limite_D(self):
        self.assertEqual(escolar.avaliar_notas(5.9, 5.9, 5.9, 5.9), "D")

    def test_avaliar_notas_minimo_D(self):
        self.assertEqual(escolar.avaliar_notas(0, 0, 0, 0), "D")

if __name__ == '__main__':
    unittest.main()