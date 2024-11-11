# 72. Escreva uma função merge_dicionarios(d1, d2) que una dois dicionários, somando os valores das chaves iguais.
def merge_dicionarios(d1, d2):
    resultado = d1.copy()  # Faz uma cópia do primeiro dicionário
    for chave, valor in d2.items():
        resultado[chave] = resultado.get(chave, 0) + valor
    return resultado

# Teste para a função merge_dicionarios
def test_merge_dicionarios():
    assert merge_dicionarios({'a': 1, 'b': 2}, {'a': 3, 'c': 4}) == {'a': 4, 'b': 2, 'c': 4}
    assert merge_dicionarios({'x': 5}, {'x': 1, 'y': 2}) == {'x': 6, 'y': 2}
    assert merge_dicionarios({}, {}) == {}
    print("test_merge_dicionarios passou!")