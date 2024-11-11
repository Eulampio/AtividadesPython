# 16. Crie uma função retira_espacos(texto) que retorne uma string sem espaços em branco.
def retira_espacos(texto):
    return texto.replace(" ", "")

# Teste da função retira_espacos
print(retira_espacos("python é legal"))  # Saída: "pythonélegal"
