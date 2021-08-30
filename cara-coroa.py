# probabilidade de cair coroa ao se jogar uma moeda

from random import choice
moeda = ["cara", "coroa"]
lado_coroa = ["coroa"]
lancamentos_feitos = 1000
numero_de_coroas = 0
for i in range(1, lancamentos_feitos + 1):
    evento = choice(moeda)
    if evento in lado_coroa:
        numero_de_coroas += 1
probabilidade = numero_de_coroas / lancamentos_feitos
print("Foram feitos %d lançamentos." % lancamentos_feitos)
print("Caiu coroa %d vezes." % numero_de_coroas)
print("A chance de cair coroa foi de %.2f." % probabilidade)