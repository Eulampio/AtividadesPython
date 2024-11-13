# 71. Crie uma função conta_elementos(lista) que retorne um dicionário com a contagem de cada elemento na lista.
from collections import Counter

def conta_elementos(lista):
    return dict(Counter(lista))

# Teste para a função conta_elementos
def test_conta_elementos():
    assert conta_elementos([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert conta_elementos(['a', 'b', 'b', 'c', 'c', 'c']) == {'a': 1, 'b': 2, 'c': 3}
    assert conta_elementos([1]) == {1: 1}
    print("test_conta_elementos passou!")
