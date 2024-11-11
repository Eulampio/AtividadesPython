# 7. Crie uma função conta_vogais(texto) que retorne o número de vogais em uma string.
def conta_vogais(texto):
    return sum(1 for letra in texto if letra.lower() in "aeiou")

# Teste da função conta_vogais
print(conta_vogais("Ola Mundo"))  # Saída: 4