# Material de referencia:
#https://realpython.com/python-return-statement/

# Função que recebe dois parametros inteiros e calcula a média
def questao_7(x,y):
    soma7 = 0
    media7 = 0
    soma7 = x + y
    media7 = (soma7)/2
    return media7

# variáveis que recebem os valores
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um valor inteiro: '))

# passa os parametros para a funçao e printa a resposta
print(questao_7(x,y))   