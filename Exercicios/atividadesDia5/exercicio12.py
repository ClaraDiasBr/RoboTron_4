# 12- Recebe o valor em dias da idade de uma pessoa e exibe em Anos, meses e dias
def questao12():
    idade = int(input('Digite sua idade em dias: '))
    idadeAnos = idade // 365
    idadeMeses = (idade % 365) // 30
    idadeDias =(idade % 365) % 30
    print('Você tem: ',idadeAnos,' anos, ', idadeMeses,' mes(es) e ',  idadeDias,' dia(s)')
    return
questao12()