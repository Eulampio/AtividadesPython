n1 = float(input("qual a primeira nota?"))
n2 = float(input("Qual a segunda nota?"))
n3 = float(input("Qual a terceira nota?"))
n4 = float(input("Qual a quarta nota?"))

media= (n1+n2+n3+n4)/4
print (media)

if media == 10: # if é se a variavel e :
    print ("aprovado com distinção")
elif media>=7: #elif se não se
    print ("aprovado")
else: # else ele diz que não tem mais testes
    print ("reprovado")


