# Importando a biblioteca panda como pd
import pandas as pd

# 'caminho' é a variável que recebe o path do arquivo .csv
caminho = 'Exercicios/atividadesDia7/csv/LndbVMRT.csv'

# Passando as informações do arquivo escolhido para uma variável chamada 'arquivo'
arquivo = pd.read_csv(caminho, encoding='UTF-8', sep=',')

# Exibir os nomes de todos os filmes exceto "The Revenant"
print(arquivo.loc[(arquivo['Movie'] != "The Revenant"), ['Movie']])