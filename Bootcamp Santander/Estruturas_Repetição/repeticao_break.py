while True:
    numero = int(input("Informe um numero:"))

    if numero == 10:
        break #usado para cortar a continuação da estrutura de repetiçaõ
    
    if numero %2 ==0:
        continue #Usado para pular uma continuação 

    print(numero)