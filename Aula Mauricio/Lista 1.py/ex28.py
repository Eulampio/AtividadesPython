# 27. Implemente uma função elementos_unicos(lista) que retorne uma lista com os elementos únicos.
def elementos_unicos(lista):
    return [x for x in lista if lista.count(x) == 1]

# Teste da função elementos_unicos
print(elementos_unicos([1, 2, 2, 3, 4, 4]))  # Saída: [1, 3]
