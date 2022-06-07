# 4- 
def comparar_idade():
    idade = int(input('Digite sua idade : '))
    if idade > 18:
        print('Maior de idadde')
    if idade < 12:
        print('Você é uma criança')
    if 12< idade < 18:
        print('Você é um adolescente')
comparar_idade()