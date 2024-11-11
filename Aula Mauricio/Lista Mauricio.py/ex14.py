# 14. Crie uma função capitaliza_palavras(texto) que capitaliza a primeira letra de cada palavra em um texto.
def capitaliza_palavras(texto):
    return " ".join([palavra.capitalize() for palavra in texto.split()])

# Teste da função capitaliza_palavras
print(capitaliza_palavras("olá mundo"))  # Saída: "Olá Mundo"
