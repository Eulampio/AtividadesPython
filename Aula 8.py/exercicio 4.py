'''Crime'''
print ("Responda as seguintes questões com S ou N")
p1=str(input("Telefonou pra vitima?"))
p2=str(input("Esteve no local do crime?"))
p3= str(input("Mora perto da vitima?"))
p4=str(input("Devia para vitima?"))
p5=str(input("Já trabalhou com a vitima?"))

cont=0



if p1== "S":
    cont=cont+1
if p2== "S":
    cont=cont+1
if p3== "S":
    cont=cont+1
if p4== "S":
    cont=cont+1
if p5== "S":
    cont=cont+1

print (cont)

if cont ==2:
    print("Suspeito")
elif cont ==3 or cont ==4:
    print("Cúmplice")
elif cont ==5:
    print ("ASSASSINO")
elif cont==1 or cont==0:
    print ("Inocente")


