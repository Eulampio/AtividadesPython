n1 = float(input("qual a primeira nota?"))
n2 = float(input("Qual a segunda nota?"))
n3 = float(input("Qual a terceira nota?"))
n4 = float(input("Qual a quarta nota?"))

media= (n1+n2+n3+n4)/4


if media >= 9.1 and media<=10:
    print ("Sua média é A", "\nAprovado")
    
elif media >=7.6 and media<= 9.0:
    print("Sua média é B","\nAprovado")

elif media >=6.0 and media >=7.5:
    print ("Sua média é C", "\nAprovado")
    
elif media >=4.1 and media <=5.9:
    print ("Sua média é D", "\nReprovado")

elif media >=4.0 and media <=0:
    print ("Sua média é E", "\nReprovado")    


