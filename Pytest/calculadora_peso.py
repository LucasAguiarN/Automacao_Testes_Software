def obter_peso_ideal(altura, sexo):
    if type(altura) != float:
        raise TypeError("Altura deve ser um número decimal.")
    elif type(sexo) != str:
        raise TypeError("Sexo deve ser uma string.")
    elif sexo not in ['M', 'F']:
        raise ValueError("Sexo deve ser 'M' ou 'F'.")
    elif altura <= 1.0 or altura >= 2.5:
        raise ValueError("Altura deve estar entre 1.0 e 2.5")
    
    if sexo == 'M':
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7