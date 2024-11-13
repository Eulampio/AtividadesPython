# 40. Escreva uma função mediana(lista) que retorne a mediana de uma lista de números.
def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        return lista[n // 2]

# Teste da função mediana
print(mediana([1, 3, 2, 4, 5]))  # Saída: 3
print(mediana([1, 3, 2, 4]))  # Saída: 2.5