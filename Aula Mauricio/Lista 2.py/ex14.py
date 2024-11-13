#14.	Desvio Padrão de Lista: Implemente uma função desvio_padrao(lista) que calcula o desvio padrão dos elementos em uma lista de números.
import math

def desvio_padrao(lista):
    if len(lista) < 2:
        raise ValueError("A lista deve ter pelo menos dois elementos")

    media = sum(lista) / len(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)
numeros = [10, 12, 23, 23, 16, 23, 21, 16]
resultado = desvio_padrao(numeros)
print(resultado)  # Saída: 4.898979485566356
