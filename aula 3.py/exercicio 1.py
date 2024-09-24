
#y = 100+10

#f=float(input("Digite a temperatura em farenheit:"))


x = (input("Qual produto desejado?"))


qtde = float (input("Quantos itens serão?"))

valor = float (input("Valor do produto?"))

porcentual = float (input(" Qual o porcentual sobre o valor do produto?"))

valortotal = (qtde * valor - qtde * valor * porcentual/100)

print("o Valor total?",valortotal)
print(f"o Valor total do produto {x} = {valortotal:.2f}")
print("o Valor total = %.2f"%(valortotal))

""" - print somente para texto
-input vai ser o leia, posso começar direto
- int para numeros inteiros
- float (real) para numeros quebrados
- Variaveis posso jogar direto 
- a forma mais facil para colocar o valor desejavel controlando os numeros após a virgula
>>> print(>> f <<"o Valor total do produto = {valortotal>>> :.2f <<<}")
 """

