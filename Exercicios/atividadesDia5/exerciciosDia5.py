# 1- Construa um programa que quando executado mostra "Hello World"
print("Hello Word")
print('-------------------------')

# 2- Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre as duas
def questao2():
    var1 = float(input('Digite uma nota : '))
    var2 = float(input('Digite uma nota : '))
    media = (var1 + var2)/2
    return media
print(questao2())
print('-------------------------')

# 3- Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar
def questao3():
    var1 = float(input('Digite um valor para saber se a média é ímpar ou par: '))
    var2 = float(input('Digite mais um valor: '))
    resultado = (var1 + var2)% 2
    if resultado == 0:
       return print("Resultado é par")
    else:
       return print("Resultado é ímpar")
questao3()
print('-------------------------')

# 4- 
def questao4():
    idade = int(input('Digite sua idade : '))
    if idade > 18:
        return print('Maior de idadde')
    if idade < 12:
        return print('Você é uma criança')
    if 12< idade < 18:
        return print('Você é um adolescente')
questao4()
print('-------------------------')

# 5- 
def questao5():
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
    return media5
print("Média dos valores pares é: ", questao5())
print('-------------------------')

# 6 
maiorQ2 = int(input('Digite um valor maior que 2: '))
if maiorQ2 > 2:
    impar=[]
    for i in range(maiorQ2, 0, -1):
        if i%2 == 1:
            impar.append(i)
    print('Os valores impares são: ' , impar)
else:
    print('ERRO!! Digite uma valor maior que 2!')
print('-------------------------')

# 7
def questao7():
    x = int(input('Digite um valor inteiro: '))
    y = int(input('Digite um valor inteiro: '))
    soma7 = x + y
    media7 = (soma7)/2
    return(media7)
print(questao7())   
print('-------------------------')
    
