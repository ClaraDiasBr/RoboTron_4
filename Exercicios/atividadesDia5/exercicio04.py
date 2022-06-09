# Função para comparar idade
def comparar_idade():
    idade = int(input('Digite sua idade : '))
    if idade > 18:
        print('Maior de idadde')
    elif idade < 12:
        print('Você é uma criança')
    elif 12< idade < 18:
        print('Você é um adolescente')

# Chama função
comparar_idade()