nome = ["edy", "gabriel", "joao"]
print(nome)

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

numeros_2 = [12,32,141,423,23141,534,12344]
quadrado = [numer **2 for numer in numeros_2]

print(quadrado)


matriz = [
    ["0", "1","2"],
    ["90", "z","2"],
    ["10", "1","53"],
    ["123", "x","2"]
]

for matrizes in matriz:
    print(matrizes)

    #metodos da classe Lista

lista = []

lista.append(1)                         
lista.append("python")
lista.append([40,90,87])
lista.clear() #usamos para limpar uma determinada lista
lista.copy() #retorna uma lista igual, só que com uma estancia diferente, ou seja, não é a mesma lista 
lista.count() #usado para informar a quantidade de vezes que um determinado objeto aparece na lista
lista.extend() #usado para somar uma nova lista
lista.index()#usado para saber qual a posição do objeto na lista
lista.pop() #usado para retirar o ultimo elemento adicionado na lista, mas eu posso colocar o indice que quero retirar
lista.remove() #usado para retirar o elemento da lista, mas referenciando o objeto em si, ao invés do indice 
lista.reverse()#serve para transpor a lista, ou seja, colocar o ultimo em primeiro e o primeiro em ultimo, dessa forma a lista vai ficar espelhada
lista.sort() #usado para organizar a lista em ordem alfabética 
lista.sort(reverse=True) #ordena de forma espelhada 
lista.sort(key=lambda x:len(x)) #função usada para por os elementos da lista em ordem crescente     
lista.sort(key=lambda x:len(x), reverse=True) #função usada para por os elementos da lista em ordem decrescente 
len(lista) #usado para tirar o tamanho da lista
sorted(lista, key=lambda x: len(x))#tambem serve para ordenar, mas a diferença é que a função sorted é Built-in
sorted(lista, key=lambda x: len(x), reverse=True)
print(lista)