def calcular_valor_final(valor):
    if valor <= 0:
        raise ValueError("O valor da compra deve ser positivo.")
    
    if valor <= 100:
        return valor
    elif valor > 100 and valor <= 500:
        return valor * 0.9
    else:
        return valor * 0.8