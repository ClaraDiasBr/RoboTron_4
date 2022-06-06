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
    soma7 = 0
    media7 = 0
    soma7 = x + y
    media7 = (soma7)/2
    return(media7)
print(questao7())   
print('-------------------------')
    
# # 8-
def questao8():
    X = int(input('Digite um valor inteiro: '))
    valor = X%2
    resposta = 0
    resultado = 1
    if valor == 0:
        print("O número é par, seu fatorial é: ")
        for i in range(1,X+1):
            resultado *=i
            fatorial = resultado
        print(fatorial)
    else:
        print("O número é ímpar, sua tabuada é: ")
        for i in range(1,11):
            resposta = i * X
            print(i, ' x ', X, ' = ', resposta)
questao8()
print('-------------------------')

# 9- 
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
print('-------------------------')   

# 10-
def questao10():
    tamanhoCesta = 3
    cesta = []
    lista = ["maça", "banana", "pera"]
    for i in range(tamanhoCesta):
        cesta.append(input('Digite uma fruta:'))
    for i in cesta:
        for j in lista:
            if i==j:
                print('Tem ', i)
    return print(cesta)
questao10()
print('-------------------------')

# 11-
def tempoJogo():
    horaInicial = int(input('Início do jogo: '))
    horaFinal = int(input('Hora que o jogo terminou: '))
    duracao = 0
    if horaFinal > horaInicial:
        duracao = horaFinal - horaInicial
        print('O JOGO DUROU ', duracao, ' HORA(S)')
    else:
        convTempo = horaFinal + 24
        duracao = convTempo - horaInicial
        print('O JOGO DUROU ', duracao, ' HORA(S)')
    return
tempoJogo()
print('-------------------------')