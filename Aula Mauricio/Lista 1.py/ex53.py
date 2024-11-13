# 53. Implemente uma função conta_ocorrencias_caracteres(s) que retorne um dicionário com a contagem de cada caractere em uma string.
def conta_ocorrencias_caracteres(s):
    return {char: s.count(char) for char in set(s)}

# Teste
print(conta_ocorrencias_caracteres("banana"))  # Saída: {'a': 3, 'n': 2, 'b': 1}
