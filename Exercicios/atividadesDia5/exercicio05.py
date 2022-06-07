# Material de referencia:
#https://www.acervolima.com.br/2021/01/recebendo-varias-entradas-do-usuario-em.html
# https://www.horadecodar.com.br/2021/01/18/como-somar-elementos-de-um-array-de-maneira-performaica/
#https://pt.stackoverflow.com/questions/230522/entrada-de-n%C3%BAmeros-na-mesma-linha-em-python

# Função que recebe 20 valores e calcula a média aritmética dos valores pares digitados
def media_valores_pares():
    X = []
    par5=[]
    tamanhoX = 20
    media5 = 0
    soma5 = 0
    for i in range(tamanhoX):
        valorDigitado = int(input('Digite um valor: '))
        X.append(valorDigitado)
        if valorDigitado%2 == 0:
            soma5 = soma5 + valorDigitado
            par5.append(valorDigitado)
    media5 = soma5/len(par5)
    print("Média dos valores pares é: ", media5)

# Chama a função
media_valores_pares()