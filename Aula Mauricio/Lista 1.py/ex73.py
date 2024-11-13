# 73. Implemente uma função filtro_dicionario(dic, valor) que retorne um novo dicionário apenas com as chaves onde os valores são maiores que valor.
def filtro_dicionario(dic, valor):
    return {k: v for k, v in dic.items() if v > valor}

# Teste para a função filtro_dicionario
def test_filtro_dicionario():
    assert filtro_dicionario({'a': 1, 'b': 3, 'c': 2}, 2) == {'b': 3}
    assert filtro_dicionario({'x': 5, 'y': 1, 'z': 4}, 3) == {'x': 5, 'z': 4}
    assert filtro_dicionario({'a': 1, 'b': 1}, 1) == {}
    print("test_filtro_dicionario passou!")