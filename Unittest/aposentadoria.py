REQUERER = 'Requerer aposentadoria'  
NAO_REQUERER = 'Não requerer'

def verificar_qualificacao_empregado(idade, tempo_de_servico):
    if type(idade) == int and type(tempo_de_servico) == int:
        if idade <= 0:
            raise ValueError("Idade Invalida")
        elif tempo_de_servico <= 0:
            raise ValueError("Tempo de Serviço Invalido")
        elif idade >= 65:
             return REQUERER
        elif tempo_de_servico >= 30:
            return REQUERER
        elif idade >= 60 and tempo_de_servico >= 25:
            return REQUERER
        return NAO_REQUERER
    else:
        raise TypeError(f'tipo incompatível')