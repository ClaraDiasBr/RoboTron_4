# 3- Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar
def par_ou_impar():
    var1 = int(input('Digite um valor: '))
    var2 = int(input('Digite mais um valor para saber se a média é ímpar ou par: '))
    resultado = (var1 + var2)% 2
    if resultado == 0:
       return print("A média é par")
    else:
       return print("A média é ímpar")
par_ou_impar()