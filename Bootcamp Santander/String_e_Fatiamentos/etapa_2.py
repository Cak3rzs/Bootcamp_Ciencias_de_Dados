#esta etapa mostrou a diferenca dos 3 usos de interpolação de variaveis, deixei a que, atualmente, é a mais ultilizada 

nome = str(input("Digite seu nome?"))
idade = int(input("Digite sua idade:"))
profissao = str(input("Digite sua profissão?"))
linguagem = str(input("Digite a linguagem que voce está aprendendo?"))
saldo = float(input("Atualmente, de quanto é o seu saldo?"))

print(f"Olá {nome}, notei que você está com {idade} anos e está trabalhando de {profissao}. Atualmente, está aprendendo {linguagem}, e que tem {saldo: 10.2f} não é mesmo?")#forma mais simples de inteporlar variaveis