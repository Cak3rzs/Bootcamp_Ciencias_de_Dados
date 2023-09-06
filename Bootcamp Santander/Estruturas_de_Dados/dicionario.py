pessoa = {"nome":"Edy", "Idade":19}

pessoa = dict(nome="Edy", Idade=19)

pessoa["telefone"] = "9999999"

print(pessoa)



contatos = {
    "edyborges534@gmail.com":{"nome":"Edy Borges", "telefone":"00000000"},
    "edyborges5123@gmail.com":{"nome":"Edy Borges", "telefone":"00000000"},
    "edyborges532@gmail.com":{"nome":"Edy Borges", "telefone":"00000000"},
    "edyborges512@gmail.com":{"nome":"Edy Borges", "telefone":"00000000"},
}

telefone = contatos["edyborges534@gmail.com"]["telefone"] 
print(telefone)

for chave in contatos:
    print(chave, contatos[chave])



for valor in contatos.items():
    print(chave, valor)


#Metodos da Classe Dict

contatos.clear() #apaga todos os valores do dicionario
contatos.copy() #vai copiar o dicionario, mas vai trazer como uma instancia diferente
contatos.fromkeys() #cria chaves no dicionario
contatos.get()#é uma segunda forma de adicionar valores dentro de um dicionario
contatos.items()#retorna uma lista de tuplas 
contatos.keys()#retorna só as chaves do dicionario
contatos.pop()#vai remover e retornar um valor 
contatos.popitem()#retira os itens na sequencia, pois n informamos qual é a chave
contatos.setdefault()#serve para add valores caso não exista
contatos.update()#para atualizar o dicionario e acrescenta valores
contatos.values()#retorna todos os valores 
resultadp = "edyborges534@gmail.com" in contatos #verifica se existe uma chave no dicionario
del contatos[""] #remove o objeto q

