# não consigo trocar m por n"
x= "ederson"
"""x= "edersom"""

# apenas em lista eu consigo mudar as variaveis realocando de lugar.
frutas=["banana", "maça", "cereja"]
frutas [0]= "pera"
frutas [-1]= "laranja"

print (frutas)

#Fatiamento mudando as variaveis na lista mudando de uma só vez 

lista =["a", "b","c","d","e","f"]
lista [1:3]= ["X", "Y"]
print (lista)

# Removendo o elemento da lista (não é a melhor forma)

lista =["a", "b","c","d","e","f"]
print (lista)
print (len(lista))
lista [1:3] =[]
print (lista)
print (len(lista))

# Inserindo um elemnto dentro da lista, EXPREMNDO A FATIA ex:[1:1]

lista = ["a","d","f"]
lista [1:1]= ["b","c"]
print(lista)
lista [4:4] = ["e"]
print(lista)

#removento o elemento de uma lista (forma mais simples) usando DEL 

lista =["a", "b","c","d","e","f"]
del lista[1]
print (lista)

lista =["a", "b","c","d","e","f"]
del lista[1:5]
print (lista)

#Operador . (ponto)! lista+ . +comando ex: a.append! append inserir elemento na lista no final
a= [81,82,83]
a.append (5)
print (a)

# sort ordenar colocar em ordem Crescente. e Reverse=true em ordem descrecente! ex:3,2,1 lista.sort()=1,2,3

a=[88,81,82,83]
a.sort()
print (a)

a.sort(reverse=True)
print (a)

# indicar o elemento na posição que o elemento está (Obs. inicia em 0). INDEX

a=[1,2,3,4,5,6,7,8] 
print (a.index(4))

# INSERT onde eu vou adicionar na posição e onde eu quero. Chamado de PILHA pareceido com o append

a=[88,81,82,83]
a.insert(1,100) # na posição 1, insira 100. A posição desejada ,(virgula) o valor
print (a)

# Count quantas vezes o elemento aparece
a=[88,81,88,82,88,88,83,86,84,74,88]
print (a)
print (a.count(88)) 

#pop remove o elemento de uma lista a.pop (remove o ultimo elemento) caso não fale a posição 
a=[88,81,88,82,88,88,83,86,84,74,88]
a.pop()
print(a)
# removendo a posição desejada
a=[88,81,88,82,88,88,83,86,84,74,88]
a.pop(0)
print (a)

#extend uma lista dentro de uma lista tornando uma jogando sempre no final
lista=[1,2]
lista.extend([3,4])
print(lista) 