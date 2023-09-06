nome = "Esther"

print(nome.upper()) #Upper é usado para deixar tudo em maiusculo
print(nome.lower()) #Lower é usado para deixar tudo em minusculo 
print(nome.title()) #Title é usado para deixar a primeira letra em maiusculo

texto = "   Olá, pessoas do meu coração!!       " 

print(texto)
print(texto.strip() + ".")  #Remove os espaços nao desejados 
print(texto.lstrip() + ".") #Remove os espaços nao desejados na esquerda
print(texto.rstrip() + ".") #Remove os espaços nao desejados na direita

curso = "Python"

print(curso.center(12, "*"))
print("-".join(curso))
