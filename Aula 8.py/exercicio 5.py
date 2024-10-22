'''Combustíveis'''

alcool= 1.90
gasolina= 2.50


litrog= float (input("quantos litros de Gasolina?"))
litroa= float (input("quantos litros de Alcool?"))



if litrog==20:
   desconto=3
   valora= (gasolina*litroa)/desconto
   print ("O valor a ser pago:", valorg)

   
elif litrog>20:
    desconto=5

if litroa<=20:
    desconto=4
    valora= (alcool*litroa)/desconto
    print ("O valor a ser pago:", valora)
elif litroa>20:
    valora= (alcool*litroa)/desconto
    print ("O valor a ser pago:", valora)
    desconto=6


