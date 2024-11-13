#26.	Ordenação com Merge Sort: Implemente uma função merge_sort(lista) que ordena uma lista usando o algoritmo de Merge Sort.
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Ordena recursivamente as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # Junta as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # Combina as duas listas ordenadas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes, se houver
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
lista = [34, 7, 23, 32, 5, 62]
resultado = merge_sort(lista)
print(resultado)  # Saída: [5, 7, 23, 32, 34, 62]