# 65. Implemente uma função dec2bin(n) que converte um número decimal para binário.
def dec2bin(n):
    return bin(n)[2:]

# Teste para a função dec2bin
def test_dec2bin():
    assert dec2bin(10) == "1010"
    assert dec2bin(0) == "0"
    assert dec2bin(255) == "11111111"
    print("test_dec2bin passou!")