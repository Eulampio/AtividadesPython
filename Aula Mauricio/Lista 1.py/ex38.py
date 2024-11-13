# 38. Crie uma função média_harmonica(lista) que calcula a média harmônica de uma lista de números.
def media_harmonica(lista):
    n = len(lista)
    soma_inversos = sum(1 / x for x in lista if x != 0)
    return n / soma_inversos if soma_inversos else 0

# Teste da função média_harmonica
print(media_harmonica([1, 2, 3, 4]))  # Saída: 1.92
print(media_harmonica([1, 0, 3]))  # Saída: 1.5
