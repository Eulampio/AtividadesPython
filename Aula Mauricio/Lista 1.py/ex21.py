# 21. Crie uma função media_lista(lista) que receba uma lista de números e retorne a média.
def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0

# Teste da função media_lista
print(media_lista([1, 2, 3, 4, 5]))  # Saída: 3.0
print(media_lista([]))  # Saída: 0