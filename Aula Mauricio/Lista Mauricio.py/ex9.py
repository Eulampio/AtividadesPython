# 9. Escreva uma função fatorial(n) que calcule o fatorial de um número inteiro n.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Teste da função fatorial
print(fatorial(5))  # Saída: 120
