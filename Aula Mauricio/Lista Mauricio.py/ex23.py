# 23. Implemente uma função menor_elemento(lista) que retorne o menor número de uma lista.
def menor_elemento(lista):
    return min(lista) if lista else None

# Teste da função menor_elemento
print(menor_elemento([1, 2, 3, 4, 5]))  # Saída: 1
print(menor_elemento([]))  # Saída: None