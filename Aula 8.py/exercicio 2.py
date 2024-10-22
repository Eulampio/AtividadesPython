'''Reajuste'''

Sal= float(input("Qual salário do mês referido?"))

if Sal <= 280.00:
    print ("aumento de 20%")
    percentual=20
elif Sal >280.00 and Sal <700.00:
    print("aumento de 15%")
    percentual=15
elif Sal >=700.00 and Sal <1500.00:
    print ("aumento de 10%")
    percentual=10
elif Sal >= 1500: 
    print ("aumento de 5%")
    percentual=5




Vaumen= Sal*percentual/100
total=Sal+Vaumen

print ("Seu salário é de:",Sal)
print ("o Percentual do aumento aplicado foi:", percentual, "%")
print (f"O Valor do aumento:{ Vaumen:.2f}")
print ("O Novo salário, após o aumento:", total)