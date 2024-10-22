cont=0
valortotal = 0
while True:

    item=input("Qual o produto?")
    itemvalor= float(input("Qual valor do item:"))

    
    valortotal=(valortotal+itemvalor)
    cont=cont+1

    print(valortotal)
    print(cont)

    if itemvalor== 0.0:
       print("Compra Finalizada")
       break

 
while True:
    
    valorpago=float(input("Valor em dinheiro?"))
   
    if valorpago < valortotal:
        print("Valor insuficiente")

    elif valorpago >=valortotal:
            troco=(valorpago-valortotal)
            print ("Troco a receber:",troco)
            print ("Volte sempre")
            break

    