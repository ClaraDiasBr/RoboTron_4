# Importando a biblioteca panda como pd
import pandas as pd

# 'caminho' é a variável que recebe o path do arquivo .csv
caminho = 'Exercicios/atividadesDia7/dados/tabelaPeriodica.csv'

# Passando as informações do arquivo escolhido para uma variável chamada 'tabela_df'
tabela_df = pd.read_csv(caminho, encoding='UTF-8', sep=',')

# Função principal
def main():
    X = int(input('Escolha um dos itens a seguir: \n1- Mostrar os Símbolos da Tabela. \n2- Pesquise um elemento pelo Símbolo. \n3- Mostrar todos elementos disponíveis. \n0- Sair da aplicação.\n'))
    if X == 1:
        mostrar_simbolo()
    if X == 2:
        listar_dados()
    if X == 3:
        mostrar_tabela()
    if X == 0:
        sair()
    else:
        opcao_indisponivel()

# Função para exibir os siímbolos da tabela periódica 
def mostrar_simbolo():
    print(tabela_df.loc[:, ["Simbolo"]])

# Função para listar informações de um elemento a partir do seu símbolo
def listar_dados():
    elemento = input('Digite o símbolo do elemento: ')
    print(tabela_df.loc[tabela_df['Simbolo'] == elemento])

# Função para mostrar os elementos contidos na tabela 
def mostrar_tabela():
    print(tabela_df)

# Função para sair da aplicação
def sair():
    print('Você saiu da aplicação!\nAté logo!')

# Função para informar que o valor digitado está errado
def opcao_indisponivel():
    print('Entre com um número válido!!!')

main()

