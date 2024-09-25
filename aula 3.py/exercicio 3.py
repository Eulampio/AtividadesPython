nome= input ("Qual seu nome:")
idade= int (input ("Qual sua idade?"))
sexo= str (input("Qual seu sexo?"))
nota1= float (input ("Qual a 1° nota?"))
nota2= float (input("Qual a 2° nota?"))


media= (nota1+nota2)/2

print (f" O(a) Aluno {nome}, de {idade} anos, do sexo {sexo}, teve a média {media:.2f} na avaliação final.")