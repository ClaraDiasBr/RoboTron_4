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

# Funçao para informar local, placar e status da partida
def local():
    estadio = partida["copa-do-brasil"][0]["estadio"]["nome_popular"]
    placar = partida["copa-do-brasil"][0]["placar"]
    status = partida["copa-do-brasil"][0]["status"]
    print('Estádio: ', estadio, "\nPlacar: ", placar,"\nStatus: ",status)

local()