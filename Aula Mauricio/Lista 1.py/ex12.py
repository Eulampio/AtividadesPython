# 12. Escreva uma função eh_palindromo(s) que verifique se uma palavra ou frase é um palíndromo.
def eh_palindromo(s):
    s = s.replace(" ", "").lower()  # Remove espaços e coloca em minúsculas
    return s == s[::-1]

# Teste da função eh_palindromo
print(eh_palindromo("arara"))  # Saída: True
print(eh_palindromo("python"))  # Saída: False