# Importando a biblioteca panda como pd
import pandas as pd

# 'caminho' é a variável que recebe o path do arquivo .csv
caminho = 'Exercicios/atividadesDia7/csv/LndbVMRT.csv'

# Passando as informações do arquivo escolhido para uma variável chamada 'arquivo'
arquivo = pd.read_csv(caminho, encoding='UTF-8', sep=',')

# Cria coluna "Movie_Year" em tempo de execução, juntando os dados movie e year
arquivo.loc[:, "Movie_Year"] = arquivo["Movie"] + " " + arquivo["Year"].astype(str)

# Exibe a coluna nova "Movie_Year"
print(arquivo['Movie_Year'])