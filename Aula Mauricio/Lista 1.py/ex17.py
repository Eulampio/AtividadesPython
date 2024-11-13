# 17. Implemente uma função encontra_palavra(texto, palavra) que retorne o índice da primeira ocorrência de uma palavra em uma string.
def encontra_palavra(texto, palavra):
    return texto.find(palavra)

# Teste da função encontra_palavra
print(encontra_palavra("Eu gosto de Python", "Python"))  # Saída: 12
