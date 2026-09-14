class Pessoa:
    def __init__(self, nome, idade):
        if not isinstance(nome, str):
            raise TypeError("O Nome deve ser uma String!")
        if not isinstance(idade, int):
            raise TypeError("A Idade deve ser um Número Inteiro.")
        if idade <= 0:
            raise ValueError("A Idade deve ser Maior que Zero.")

        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def verificacao_maioridade(self):
        return self.__idade >= 18