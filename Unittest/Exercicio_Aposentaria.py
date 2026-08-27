import unittest
import aposentadoria

class TestAposentadoria(unittest.TestCase):
    def test_verificar_qualificacao_idade_invalida(self):
        self.assertRaisesRegex(ValueError, "Idade Invalida", aposentadoria.verificar_qualificacao_empregado, 0, 10)

    def test_verificar_qualificacao_tempo_servico_invalido(self):
        self.assertRaisesRegex(ValueError, "Tempo de Serviço Invalido", aposentadoria.verificar_qualificacao_empregado, 20, 0)

    def test_verificar_qualificacao_idade_nao_inteira(self):
        self.assertRaises(TypeError, aposentadoria.verificar_qualificacao_empregado, "65", 30)

    def test_verificar_qualificacao_tempo_servico_nao_inteiro(self):
        self.assertRaises(TypeError, aposentadoria.verificar_qualificacao_empregado, 30, "65")

    def test_verificar_qualificacao_por_idade(self):
        self.assertEqual(aposentadoria.verificar_qualificacao_empregado(65, 20), "Requerer aposentadoria")

    def test_verificar_qualificacao_por_tempo_servico(self):
        self.assertEqual(aposentadoria.verificar_qualificacao_empregado(59, 30), "Requerer aposentadoria")

    def test_verificar_qualificacao_por_idade_e_tempo_servico(self):
        self.assertEqual(aposentadoria.verificar_qualificacao_empregado(60, 25), "Requerer aposentadoria")

    def test_verificar_qualificacao_nao_qualificado(self):
        self.assertEqual(aposentadoria.verificar_qualificacao_empregado(54, 24), "Não requerer")

if __name__ == '__main__':
    unittest.main()