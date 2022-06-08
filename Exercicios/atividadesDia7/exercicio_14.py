# Importando a biblioteca panda como pd
import pandas as pd

# 'caminho' é a variável que recebe o path do arquivo .csv
caminho = 'Exercicios/atividadesDia7/csv/LndbVMRT.csv'

# Passando as informações do arquivo escolhido para uma variável chamada 'arquivo'
arquivo = pd.read_csv(caminho, encoding='UTF-8', sep=',')

# Exibir os nomes e idades dos atores definidos no intervalo de 1987 até 1999
print(arquivo.loc[(arquivo['Year'] >= 1987) & (arquivo['Year'] <= 1999), ['Name', 'Age']])