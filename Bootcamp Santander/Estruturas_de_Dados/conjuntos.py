set() #set é uma coleção que nao possui objetos repitidos, ou seja, quando rodarmos este set, ele irá ignorar todos os numeros repetidos

numeros = {1,2,3,4,5,6,6,6,7,2,2,1}
print(numeros)

for numero in numeros:
    print(numero)


conjunto_a = {2,4,5,6}
conjunto_b = {1,3,5,7}

conjunto_a.union(conjunto_b)#uniao de conjuntos
conjunto_a.intersection(conjunto_b)#pega a parte igual dos conjuntos
conjunto_a.difference(conjunto_b)#tudo que eu tenho no meu conjunto, que nao está no outro
conjunto_a.symmetric_difference(conjunto_b)#tudo que eu tenho de diferente dos meus conjuntos
conjunto_a.issubset(conjunto_b)#todos os elementos de um conjunto estão no outro
conjunto_a.isdisjoint(conjunto_b)#são conjuntos onde eles nao se tocam, ou seja, todos os elementos não são repetidos
conjunto_a.add()#usada para adicionar algo ao conjunto
conjunto_a.clear()#usado para limpar
conjunto_a.copy() #vai copiar mas irá criar uma nova instancia 
conjunto_a.discard()#serve para descartar os valores
conjunto_a.pop() #vai retirando os valores do conjunto
conjunto_a.remove()#serve para descartar os valores, mas a diferença é que, caso o valor não exista, o terminal irá informar o erro
conjunto_a.len() #serve para tirar o tamanho do conjunto

