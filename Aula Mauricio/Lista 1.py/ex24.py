# 24. Crie uma função conta_ocorrencias(lista, elemento) que conta quantas vezes um elemento aparece em uma lista.
def conta_ocorrencias(lista, elemento):
    return lista.count(elemento)

# Teste da função conta_ocorrencias
print(conta_ocorrencias([1, 2, 3, 2, 2, 4], 2))  # Saída: 3
print(conta_ocorrencias([1, 2, 3, 4], 5))  # Saída: 0