conta_normal = False
conta_universitaria = False
conta_black = True

saldo = 2000
saque = 1500
cheque_especial = 450


if conta_normal: 
    if saldo >= saque: 
        print("Saque realizado com sucesso")
    elif saque <= (saldo +cheque_especial):
        print("Saque realizado em cheque especial")
    else:
        print("Não foi possivel realizar o saque, Saldo Insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Saldo Insuficiente")
elif conta_black:
    print("Conta Black selecionadad, Seja bem-Vindo")
else:
    print("Não foi possivel reconhecer sua conta. Tente novamente ")
