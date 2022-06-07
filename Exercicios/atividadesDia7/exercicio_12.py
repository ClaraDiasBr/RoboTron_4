# Importando a biblioteca panda como pd
import pandas as pd

# 'caminho' é a variável que recebe o path do arquivo .csv
caminho = 'Exercicios/atividadesDia7/csv/LndbVMRT.csv'

# Passando as informações do arquivo escolhido para uma variável chamada 'arquivo'
arquivo = pd.read_csv(caminho, encoding='UTF-8', sep=',')

# Exibir o nome dos atores que ganharam o Oscar em 1991 e 2016
print(arquivo.loc[(arquivo['Year'] == 1991) | (arquivo['Year'] == 2016), ['Name']])