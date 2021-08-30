# probabilidade de cair par ao se jogar um dado 

import random
dado = [1, 2, 3, 4, 5, 6]
pares = [2, 4, 6]
contador = 0
numero_de_lancamentos = 1000
for i in range(1, numero_de_lancamentos + 1):
    aleatorio = random.choice(dado)
    if aleatorio in pares:
        contador += 1
probabilidade = contador / numero_de_lancamentos
print("Foram feitos %d lançamentos com um dado de 6 faces." % numero_de_lancamentos)
print("%d dos resultados observados são pares." % contador)
print("A chance de cair par é de %.2f." % probabilidade)
