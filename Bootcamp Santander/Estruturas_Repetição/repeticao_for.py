#Exemplo ultilizando um interável
exto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")
else:
    print()


#Exemplo com Range, é uma funçaõ built-in 
for numero in range(10000000000, 1):
    print(numero)


 