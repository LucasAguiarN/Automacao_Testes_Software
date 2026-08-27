import unittest
import aposentadoria

class TestAposentadoria(unittest.TestCase):
    def test_verificar_qualificacao_idade_invalida(self):
        self.assertRaisesRegex(ValueError, "Idade Invalida", aposentadoria.verificar_qualificacao_empregado(0, 10))

    def test_verificar_qualificacao_tempo_servico_invalido(self):
        self.assertRaisesRegex(ValueError, "Tempo de Serviço Invalido", aposentadoria.verificar_qualificacao_empregado(20, 0))