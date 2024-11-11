# 36. Implemente uma função eh_perfeito(n) que verifica se um número é um número perfeito.
def eh_perfeito(n):
    divisores = [i for i in range(1, n) if n % i == 0]
    return sum(divisores) == n

# Teste da função eh_perfeito
print(eh_perfeito(6))  # Saída: True (6 é perfeito)
print(eh_perfeito(10))  # Saída: False