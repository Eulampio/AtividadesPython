# 25. Escreva uma função remove_duplicados(lista) que retorne uma lista sem elementos duplicados.
def remove_duplicados(lista):
    return list(set(lista))

# Teste da função remove_duplicados
print(remove_duplicados([1, 2, 2, 3, 3, 4]))  # Saída: [1, 2, 3, 4]
