# 2- Função que recebe duas variaveis notas e apresenta a média entre as duas
def media_notas():
    nota1 = float(input('Digite uma nota : '))
    nota2 = float(input('Digite uma nota : '))
    media = (nota1 + nota2)/2
    print(media)
# Chama a função
media_notas()