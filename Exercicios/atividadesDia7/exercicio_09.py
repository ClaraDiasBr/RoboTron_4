# Importando a biblioteca panda como pd
import pandas as pd

# 'caminho' é a variável que recebe o path do arquivo .csv
caminho = 'Exercicios/atividadesDia7/csv/LndbVMRT.csv'

# Lendo as informações da coluna 'Age'
idade = pd.read_csv(caminho, encoding='UTF-8', sep=',', usecols=["Age"])

# Exibir no terminal o que está dentro de 'idade' 
print(idade)