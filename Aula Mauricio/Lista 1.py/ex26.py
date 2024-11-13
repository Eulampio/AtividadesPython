# 26. Crie uma função soma_pares(lista) que retorne a soma de todos os números pares em uma lista.
def soma_pares(lista):
    return sum(x for x in lista if x % 2 == 0)

# Teste da função soma_pares
print(soma_pares([1, 2, 3, 4, 5, 6]))  # Saída: 12