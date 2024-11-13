# 57. Implemente uma função substitui_espaco(texto, simbolo) que substitua todos os espaços em uma string por um símbolo específico.
def substitui_espaco(texto, simbolo):
    return texto.replace(" ", simbolo)

# Teste
print(substitui_espaco("Olá Mundo", "-"))  # Saída: Olá-Mundo

