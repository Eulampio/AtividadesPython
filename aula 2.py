'''int( inteiro ex: 10)
float (real ex:15.5)
bool (verdadeiro ou falso)
str (cadeia)
input direto é string(ex: input= )'''

'''nome= input (" digite o nome:")
print (nome)
idade=input ("Digite sua idade:")
print (type (idade))'''

"""salario= int(input("Salário?"))
imposto= float (input(" Digite o imposto="))"""

"""sal= float(input("digite salario:"))
print (sal)"""
# %d-Inteiro
# %s-string
# %f-float
# %b-bool

'''idade1=10
idade2=3
filhos=2
print ("eu tenho", filhos, "amobos de",idade1, "e",idade2," anos")
print ("eu tenho %d filhos, amobos de %d e %d anos" % (4,5,3)) # coloca a variavel de forma seguencial
print ("eu tenho %d filhos, amobos de %d e %d anos" % (filhos, idade1, idade2)) #  % coloca a variavel 

Z=1755/111
print ("% .0F"% Z)  # % e .(e o numero) é a quantidade numeros após o ponto
print ("% .1F"% Z)
print ("% .10F"% Z)'''

#"""""""" concatenação""""""""
#    sinal de mais(+ quando aplica duas cadeias)

"""a= "Ederson"
b= "Costa"
print ("Prezado "+a+" "+b+"."+"olá")
print (" Prezado %s %s. Olá"% (a,b))
print ("Prezado ",a,b,".","olá")

num1 = 10
num2 = 10

print (num1+num2)
print (10*"Ederson\n")"""

#""""Replicação de Strings""""

# print ("+"+10*"-"+"+")
# print (("|"+" "*10+"|\n")*5,end="")
# print ("+"+ 10*"-"+"+")

"""print(" "*5+"♥♥♥♥"+4*" "+4*"♥")
print(" "*4+5*"♥"+4*" "+5*"♥")
print(" "*3+7*"♥"+2*" "+7*"♥")

print(" "*3+7*"♥"+2*" "+7*"♥")

print (" ♥"+6*"  ♥")
print ("♥" +7* "  ♥")
print ("  ♥"+4*"   ♥")
print("    ♥"+3*"   ♥")
print("     ♥"+2*"    ♥")
print("       ♥"+1*"     ♥")
print("        ♥"+"  ♥")
print("          ♥")"""

"""frase='um triangulo de base igual {0} e altura igual a {1} possui area igual a {2}.'.format (3,4,12)
print (frase)"""

"""linguagem= "PYTHON"
frase=(f"programando em {linguagem}")
print (frase)

x=(2/3)
print (f"printando o {x}")
print (f" printando o{x:.2f}")"""

f=float(input("Digite a temperatura em farenheit:"))
c= (5/9)*(f-32)
print (f"valor em Celsius {c:.2}")



real f
escreva("digite f")
leia(f)


f = float (input ("digite f"))