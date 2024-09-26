# Contar dentro da str , quantidade de Caracters (len)
a="ederson"
print (len(a))
# outra forma de escrever
b= (len(a))
print (b)

# transformando a 1° letra do texto em Maiúsculo (.capitalize)
print (a.capitalize())

# transformando todo texto em Maiúsculo (.upper)
a= "ederson"
print (a.upper())
#b= a.upper() >> duvida questionar

# transformando todo texto em Minusculo (.casefold ou .lower)

a="EDERSON"
print (a.casefold())
# outra forma, jogar a variavel no final da frase
print ("ederson".casefold())
print ("ederson".lower())

# islower questionar a variavel se é verdadeiro ou falso "IS"
a= "EDERSON"
print (a.islower())
print (a.isupper())

# verificando se a str possui numeros inteiros (.ISDIGIT)

a="123456"
print (a.isdigit())
a= "1234asv"
print (a.isdigit())

#Substituição de uma str (.replace)

a= "Ederson Roberto"
print(a.replace("Roberto","Costa"))

#Separação de uma str (.Split)

a="Ederson#Roberto Costa"
print(a.split('#'))
print(a)

#encontre a posição na str (.find) lembrando que ele vai encontar a 1° posição

a="Ederson Roberto Costa"
print (a.find("Costa"))

# verificando se dentro da variavel a informação é verdade ou false

a="Ederson Roberto Costa"
print(" Costa"in a)

#frequencia de ocorrencia de um parametro (.count)

a="Ederson Roberto Costa"
print (a.count("o"))

# contando o numero de casas de uma str (.s)
# da direita pra esqueda começo com 0. Da esquerda pra direita começo com -1
#sempre em chaves []

#ola, mundo! (contando espaço tbm)
#12345678910

s="Olá, Mundo!"
print(s[0])
print(s[2])
print(s[6])
#Da esquerda pra direita fica em ordem descente.
s="Ola, Mundo!"
print (s[-11])
print (s[-9])
print (s[-5])

#pegar apenas uma "fatia" (slice - : + ) 
s="Ola, Mundo!"
print (s[1:3])
