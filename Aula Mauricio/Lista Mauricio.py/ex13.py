# 13. Implemente uma função conta_letras(s, letra) que conte quantas vezes uma determinada letra aparece em uma string.
def conta_letras(s, letra):
    return s.count(letra)

# Teste da função conta_letras
print(conta_letras("banana", "a"))  # Saída: 3
