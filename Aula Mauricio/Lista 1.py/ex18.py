# 18. Escreva uma função alterna_maiusculas(texto) que alterne as letras para maiúsculas e minúsculas.
def alterna_maiusculas(texto):
    return "".join([letra.upper() if i % 2 == 0 else letra.lower() for i, letra in enumerate(texto)])

# Teste da função alterna_maiusculas
print(alterna_maiusculas("python"))  # Saída: "PyThOn"
