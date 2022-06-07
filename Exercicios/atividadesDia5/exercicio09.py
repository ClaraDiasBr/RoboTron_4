# Material de referencia:
#https://www.delftstack.com/pt/howto/python/python-reverse-a-list/

# Função que recebe 15 valores de entrada, e no final mostra os valores de forma invertida
def questao9():
    tamanho = 15
    X = []
    for i in range(0,tamanho):
        valorDigitado = int(input('Digite um valor: '))
        X.append(valorDigitado)
        i +=1
    newX = X[::-1]
    return print(newX)        
questao9()