import pytest
from src.pessoa import Pessoa


def test_get_nome():
    pessoa = Pessoa("Lucas", 18)
    assert pessoa.get_nome() == "Lucas"

def test_get_idade():
    pessoa = Pessoa("Lucas", 18)
    assert pessoa.get_idade() == 18

def test_verificacao_maioridade_positiva():
    pessoa = Pessoa("Lucas", 18)
    assert pessoa.verificacao_maioridade() == True

def test_verificacao_maioridade_negativa():
    pessoa = Pessoa("Lucas", 17)
    assert pessoa.verificacao_maioridade() == False

def test_type_nome_invalido():
    with pytest.raises(TypeError):
        Pessoa(10, 18)

def test_type_idade_invalida():
    with pytest.raises(TypeError):
        Pessoa("Lucas", "18")

def test_idade_negativa():
    with pytest.raises(ValueError):
        Pessoa("Lucas", -1)