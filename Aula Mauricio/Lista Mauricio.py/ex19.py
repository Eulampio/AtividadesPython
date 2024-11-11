# 19. Crie uma função apaga_vogais(s) que remova todas as vogais de uma string.
def apaga_vogais(s):
    return "".join([letra for letra in s if letra not in "aeiouAEIOU"])

# Teste da função apaga_vogais
print(apaga_vogais("banana"))  # Saída: "bn"
