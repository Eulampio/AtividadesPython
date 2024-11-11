# 43. Escreva uma função recursiva produto(a, b) que multiplica dois números inteiros a e b.
def produto(a, b):
    if b == 0:
        return 0
    return a + produto(a, b-1)

# Teste
print(produto(3, 4))  # Saída: 12

