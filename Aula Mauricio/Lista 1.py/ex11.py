# 11. Crie uma função conta_palavras(texto) que conte quantas palavras existem em uma string.
def conta_palavras(texto):
    return len(texto.split())

# Teste da função conta_palavras
print(conta_palavras("Eu gosto de Python"))  # Saída: 4
