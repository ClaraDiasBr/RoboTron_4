# 8- ARRUMAR!!!
def questao8():
    X = int(input('Digite um valor inteiro: '))
    valor = X % 2
    if valor == 0:
        print("O número é par, seu fatorial é: ")
        fatorial(X)
    else:
        print("O número é ímpar, sua tabuada é: ")
        tabuada(X)
        

def fatorial(X):
    resultado = 1
    for i in range(1,X+1):
            resultado *=i
            fatorial = resultado
    return fatorial

def tabuada(X):
    resposta = 0
    for i in range(1,11):
            resposta = i * X
            print(i, ' x ', X, ' = ', resposta)
    
    

questao8()