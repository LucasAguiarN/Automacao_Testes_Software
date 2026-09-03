def calcular_imc(nome, peso, altura):
    imc = peso / (altura**2)
    if not isinstance(peso, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Peso e altura devem ser números")
    if imc < 18.5:
        return f'{nome} seu IMC é Abaixo do Peso'
    elif imc >= 18.5 and imc <= 24.9:
        return f'{nome} seu IMC é Peso Normal'
    elif imc >= 25.0 and imc <= 29.9:
        return f'{nome} seu IMC é Sobrepeso'
    elif imc >= 30.0 and imc <= 34.9:
        return f'{nome} seu IMC é Obesidade Grau I'
    elif imc >= 35.0 and imc <= 39.9:
        return f'{nome} seu IMC é Obesidade Grau II'
    elif imc >= 40:
        return f'{nome} seu IMC é Obesidade Grau III'