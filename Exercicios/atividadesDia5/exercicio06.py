# 6 
maiorQ2 = int(input('Digite um valor maior que 2: '))
if maiorQ2 > 2:
    impar=[]
    for i in range(maiorQ2, 0, -1):
        if i%2 == 1:
            impar.append(i)
    print('Os valores impares são: ' , impar)
else:
    print('ERRO!! Digite uma valor maior que 2!')