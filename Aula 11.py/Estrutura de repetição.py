# Python For
''' no cód recorremos a lista em nomes e imprimimos cada elemento, a variavel define na linha 1 é uma lista inicializada com seguencia '''
nomes= "Ederson"
for n in nomes:
    print (n)

nomes= ["Pedro", "Joao", "Leticia"]
for n in nomes:
    print (n)

# For break, repete ate o ultimo selecionado

nomes= ["Pedro", "Joao", "Leticia"]# no caso, a ordem dada é de repetir até joao
for n in nomes:
    print (n)
    if n == "Joao":
        break 
    print(n)# pra não repetir joao e parar antes dentro do inf 

#For Continue

nomes= ["Pedro", "Joao", "Leticia"]# no caso, a ordem dada é de repetir sem o joao
for n in nomes:
    print (n)
    if n == "Joao":
        continue

x=10
while x>0:
    x=x-1
    if x==5:
        continue
    print (x)

#FOR Função Range (determinando o numero de vezes começando em 0 e incrementos em 1 e termina em numero especificado )

for x in range (6):
    print (x)

"""nomes= ["Pedro", "Joao", "Leticia"]
for n in nomes:
    print (x,nomes[x])"""

for x in range (2,6):# (dado o valor inicial 2 e valor final 6 porem não é incluso)
    print(x)

for x in range (2,10,2):# Incremento vai pulando no caso de 2 em 2. começa em 2 ao 8(no caso) e pula(2,4,6)
    print(x)

#LOOP aninhado (será executado para cada interação)

for i in range(5):
    for j in range(6):
        print (i,j)