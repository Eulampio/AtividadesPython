# 37. Escreva uma função eh_armstrong(n) que verifica se um número é um número de Armstrong.
def eh_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    soma = sum(int(digit) ** num_len for digit in num_str)
    return soma == n

# Teste da função eh_armstrong
print(eh_armstrong(153))  # Saída: True
print(eh_armstrong(370))  # Saída: True
print(eh_armstrong(123))  # Saída: False