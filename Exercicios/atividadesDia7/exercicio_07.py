# Importa biblioteca json
import json

# Abre o arquivo json nomeando-o de campeonato e guarda em campeonato_json
arquivo = 'Exercicios/atividadesDia7/json/GxdV3pRP.json'
def abrir_campeonato():
    with open(arquivo, encoding='utf-8') as campeonato:
        campeonato_json = json.load(campeonato)
        return campeonato_json
retorna_campeonato = abrir_campeonato()

# Funcao que percorre as principais chaves do arquivo
def chaves_principais():
    for key, value in retorna_campeonato.items():
        print(key, ":", value)

chaves_principais()
