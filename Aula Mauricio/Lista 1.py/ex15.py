# 15. Escreva uma função ocorrencias_palavras(texto) que retorne um dicionário com a contagem de cada palavra em um texto.
def ocorrencias_palavras(texto):
    palavras = texto.split()
    return {palavra: palavras.count(palavra) for palavra in palavras}

# Teste da função ocorrencias_palavras
print(ocorrencias_palavras("python é legal e python é divertido"))
# Saída: {'python': 2, 'é': 2, 'legal': 1, 'e': 1, 'divertido': 1}
