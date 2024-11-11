# 30. Implemente uma função uniao_listas(lista1, lista2) que retorne a união de duas listas.
def uniao_listas(lista1, lista2):
    return list(set(lista1) | set(lista2))

# Teste da função uniao_listas
print(uniao_listas([1, 2, 3], [3, 4, 5]))  # Saída: [1, 2, 3, 4, 5]
