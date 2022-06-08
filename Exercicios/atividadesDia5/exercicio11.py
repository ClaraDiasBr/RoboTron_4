# 11- Calcula o tempo do jogo
def tempoJogo():
    horaInicial = int(input('Início do jogo: '))
    horaFinal = int(input('Hora que o jogo terminou: '))
    duracao = 0
    if horaFinal > horaInicial:
        duracao = horaFinal - horaInicial
        print('O JOGO DUROU ', duracao, ' HORA(S)')
    else:
        convTempo = horaFinal + 24
        duracao = convTempo - horaInicial
        print('O JOGO DUROU ', duracao, ' HORA(S)')
    return
tempoJogo()