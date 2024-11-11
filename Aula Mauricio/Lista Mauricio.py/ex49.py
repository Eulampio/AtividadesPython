# 49. Escreva uma função mdc_lista(lista) que retorne o maior divisor comum entre os números de uma lista.
from functools import reduce
from math import gcd
def mdc_lista(lista):
    return reduce(gcd, lista)

# Teste
print(mdc_lista([48, 18, 30]))  # Saída: 6
