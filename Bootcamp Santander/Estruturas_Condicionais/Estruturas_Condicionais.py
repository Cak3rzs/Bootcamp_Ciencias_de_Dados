#USO DO IF SIMPLES, ALÉM DO ELSE E ELIF
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Parabens! Voçe é maior de idade")

if idade < MAIOR_IDADE:
    print("Menor de idade")


if idade >= MAIOR_IDADE:
    print("Parabens! Voçe é maior de idade")
else:
    print("Menor de idadae")


if idade >= MAIOR_IDADE:
    print("Parabens! Voçe é maior de idade")
elif idade == IDADE_ESPECIAL:
    print("Daqui um ano voce será maior de idade! Parabens :D")
