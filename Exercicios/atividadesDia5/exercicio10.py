# Função para comparar "lista" e "cesta"
def questao10():
    tamanhoCesta = 3
    cesta = []
    lista = ["maça", "banana", "pera"]
    for i in range(tamanhoCesta):
        cesta.append(input('Digite uma fruta:'))
    for i in cesta:
        for j in lista:
            if i==j:
                print('Tem ', i)
    return print(cesta)
questao10()