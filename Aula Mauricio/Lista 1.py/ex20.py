# 20. Implemente uma função troca_vogais(s, nova_letra) que substitua todas as vogais de uma string por uma nova letra.
def troca_vogais(s, nova_letra):
    return "".join([nova_letra if letra in "aeiouAEIOU" else letra for letra in s])

# Teste da função troca_vogais
print(troca_vogais("banana", "x"))  # Saída: "bxnxnx"