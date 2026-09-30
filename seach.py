def search_line(array, valor):
    list_indice = []
    for i in range(len(array)):
        if array[i] == valor:
            list_indice.append(i)
    return list_indice

def search_binary(array, valor):
    inicio = 0
    final = len(array) - 1

    while inicio <= final:
        meio = (inicio + final) // 2
        if array[meio] == valor:
            return meio
        if valor > array[meio]:
            inicio = meio + 1
        else:
            final = meio - 1

    return -1
