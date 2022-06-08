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

# Funçao para encontrar o vencedor
def vencedor():
    placar_mandante = partida["copa-do-brasil"][0]["placar_mandante"]
    placar_visitante = partida["copa-do-brasil"][0]["placar_visitante"]
    if placar_mandante > placar_visitante:
        vencedor = partida["copa-do-brasil"][0]["time_mandante"]["nome_popular"]
        print("Vencedor: ",vencedor)
    if placar_mandante < placar_visitante:
        vencedor = partida["copa-do-brasil"][0]["time_visitante"]["nome_popular"]
        print("Vencedor: ",vencedor)
    if placar_mandante == placar_visitante:
        print('Empate')
vencedor()