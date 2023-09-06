def ler_mensagem():
    str(input("Digite seu nome:"))

def chamar_mensagem():
    print(ler_mensagem)

def mostrar_mensagem():
    print(f"Olá{chamar_mensagem}!!!")


ler_mensagem()
chamar_mensagem()
mostrar_mensagem()
