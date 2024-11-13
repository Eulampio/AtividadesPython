# 3. Escreva uma função eh_par(numero) que receba um número e retorne True se ele for par e False caso contrário.
def eh_par(numero):
    return numero % 2 == 0

# Teste da função eh_par
print(eh_par(4))  # Saída: True
print(eh_par(5))  # Saída: False