# 29. Crie uma função intersecao_listas(lista1, lista2) que retorne os elementos em comum entre duas listas.
def intersecao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Teste da função intersecao_listas
print(intersecao_listas([1, 2, 3], [3, 4, 5]))  # Saída: [3]
