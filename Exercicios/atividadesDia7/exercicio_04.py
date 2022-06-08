# Importa biblioteca json
import json

# Variável que recebe o caminho do arquivo json
arquivo = 'Exercicios/atividadesDia7/json/amF0XHEa.json'

# Função para abrir o arquivo json nomeando-o de partida e guarda em partida_json
def abrir_partida():
    with open(arquivo, encoding='utf-8') as partida:
        partida_json = json.load(partida)
        return partida_json
partida = abrir_partida()

# Funçao para mostrar as informaçoes do visitante
def inf_visitante():
    visitante = partida["copa-do-brasil"][0]["time_visitante"]
    print(visitante)
inf_visitante()