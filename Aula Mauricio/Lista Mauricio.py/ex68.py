# 68. Implemente uma função tamanho_arquivo(nome_arquivo) que retorne o tamanho de um arquivo em bytes.
import os

def tamanho_arquivo(nome_arquivo):
    return os.path.getsize(nome_arquivo)

# Teste para a função tamanho_arquivo
def test_tamanho_arquivo():
    with open('teste.txt', 'w') as f:
        f.write("Este é um arquivo de teste.")
    assert tamanho_arquivo('teste.txt') == 22
    os.remove('teste.txt')
    print("test_tamanho_arquivo passou!")
