# Na condição AND para ser True tudo tem que ser true 
#Na condição OR para ser True, apenas um tem que ser True
print (True and False)
print (True and True )
print(False and False)
print (True or False)
print (True or True)
print (False or False)
saldo = 1000
saque = 250 
limite = 200
conta_especial = True

expressao = (saque >= saque and  saque <= limite) or (conta_especial and saldo >= saque)

expressao_2 = saque >= saque and  saque <= limite or conta_especial and saldo >= saque

conta_normal_com_saldo_suficiente = (saque >= saque and  saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(expressao)
print(expressao_2) 
print(expressao_3)



