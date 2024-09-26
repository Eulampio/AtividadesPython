import os 
nome= input ("qual seu nome?")
cpf = str (input(" qual seu cpf?"))
rg= str (input (" qual seu rg?"))
data= str (input (" qual a sua data de nascimento?"))
sexo= input ("qual seu sexo?")
peso= float (input(" qual seu peso?"))
sangue= str (input (" qual seu tipo sanguineo?"))
renda= float (input("qual sua renda?"))
endereco= str (input (" qual seu endereço?"))
telefone= str (input (" qual seu telefone?"))
cidade= input ("qual sua cidade?")
estado= input ("qual seu estado?")
os.system('cls')
print ("+"+20*"-"+"+")
print (f" \t\tCadastro\n\n  Eu {nome}, portadora do cpf{cpf}, e RG {rg}.
       Nacida na data de {data}, do sexo {sexo}, pensando {peso}, tipo sanguineo {sangue},
         com  a renda de R$ {renda}. Locada no endereço {endereco}.
           Telefone para contato: {telefone}  ")
print ("+"+ 20*"-"+"+")