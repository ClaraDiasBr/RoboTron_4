# Importa biblioteca json
import json

# Variável que recebe o caminho do arquivo json
arquivo = 'Exercicios/atividadesDia7/json/amF0XHEa.json'

# Função para abrir o arquivo json nomeando-o de partida e guarda em partida_json
def abrir_partida():
    with open(arquivo, encoding='utf-8') as partida:
        partida_json = json.load(partida)
        return partida_json
retorna_partida = abrir_partida()
print(retorna_partida)