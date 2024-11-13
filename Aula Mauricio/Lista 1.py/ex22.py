# 22. Escreva uma função maior_elemento(lista) que retorne o maior número de uma lista.
def maior_elemento(lista):
    return max(lista) if lista else None

# Teste da função maior_elemento
print(maior_elemento([1, 2, 3, 4, 5]))  # Saída: 5
print(maior_elemento([]))  # Saída: None