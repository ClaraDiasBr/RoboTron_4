# Material de referencia:
# https://www.freecodecamp.org/portuguese/news/ler-arquivos-json-em-python-como-usar-load-loads-e-dump-dumps-com-arquivos-json/
# https://pynative.com/python-json-load-and-loads-to-parse-json/#:~:text=Parameter%20used%3A-,The%20json.,document%20into%20the%20Python%20dictionary


# Importa biblioteca json
import json

# Abre o arquivo json nomeando-o de campeonato e guarda em campeonato_json
arquivo = 'Exercicios/atividadesDia7/json/GxdV3pRP.json'
def abrir_campeonato():
    with open(arquivo, encoding='utf-8') as campeonato:
        campeonato_json = json.load(campeonato)
        return campeonato_json
retorna_campeonato = abrir_campeonato()

# Funçao para informar edicao da partida
def edicao():
    edicao = retorna_campeonato["edicao_atual"]
    print("Edição Atual:")
    for key, value in edicao.items():
        print(key, ":", value)

# Funçao para informar fase da partida
def fase():
    fase = retorna_campeonato["fase_atual"]
    print("\nFase Atual:")
    for key, value in fase.items():
        print(key, ":", value)

# Funçao para informar rodada da partida
def rodada():
    rodada = retorna_campeonato["rodada_atual"]
    print("\nRodada Atual:")
    for key, value in rodada.items():
        print(key, ":", value)

# Chamando as funcoes
edicao()
fase()
rodada()