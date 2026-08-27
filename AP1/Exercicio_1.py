def divisao(a, b):
    if b == 0:
        raise ValueError("Divisor deve ser maior que zero.")
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os inputs devem ser números inteiros ou floats.")
    else:
        return a / b