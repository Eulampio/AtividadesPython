# 10. Crie uma função eh_primo(n) que verifique se um número é primo.
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Teste da função eh_primo
print(eh_primo(7))  # Saída: True
print(eh_primo(10))  # Saída: False
