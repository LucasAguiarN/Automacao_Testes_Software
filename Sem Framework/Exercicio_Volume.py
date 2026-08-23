def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura

#Conta 1
try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print("Calculo Conta #1 Correto!")
except AssertionError:
    print("Calculo Conta #1 Incorreto!")

#Conta 2
try:
    resultado = calcula_volume(2, 4, 3)
    assert resultado == 24
    print("Calculo Conta #2 Correto!")
except AssertionError: 
    print("Calculo Conta #2 Incorreto!")

#Conta 3
try:
    resultado = calcula_volume(5, 5, 2)
    assert resultado == 100
    print("Calculo Conta #3 Correto!")
except AssertionError: 
    print("Calculo Conta #3 Incorreto!")