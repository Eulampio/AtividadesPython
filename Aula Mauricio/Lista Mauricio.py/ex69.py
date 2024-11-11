# 69. Escreva uma função minimax(lista) que retorne o menor e o maior número de uma lista.
def minimax(lista):
    return min(lista), max(lista)

# Teste para a função minimax
def test_minimax():
    assert minimax([1, 2, 3, 4, 5]) == (1, 5)
    assert minimax([5, 4, 3, 2, 1]) == (1, 5)
    assert minimax([7]) == (7, 7)
    print("test_minimax passou!")
