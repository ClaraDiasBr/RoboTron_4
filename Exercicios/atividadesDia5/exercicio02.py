# 2- Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre as duas
def media_notas():
    nota1 = float(input('Digite uma nota : '))
    nota2 = float(input('Digite uma nota : '))
    media = (nota1 + nota2)/2
    print(media)
media_notas()