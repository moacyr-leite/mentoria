def bubble_sort(array):
    trocou = False
    for i in range(len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                trocou = True
        if not trocou:
            print("Não houve troca!")
            return array
    return array

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid_left = merge_sort(array[:len(array)//2])
    mid_right = merge_sort(array[len(array)//2:])
    i=j=k=0
    while i < len(mid_left) and j < len(mid_right):
        if mid_left[i] < mid_right[j]:
            array[k] = mid_left[i]
            i += 1
        else:
            array[k] = mid_right[j]
            j += 1
        k += 1

    # Verifica se restou algum elemento na metade esquerda
    while i < len(mid_left):
        array[k] = mid_left[i]
        i += 1
        k += 1

    # Verifica se restou algum elemento na metade direita
    while j < len(mid_right):
        array[k] = mid_right[j]
        j += 1
        k += 1

    return array

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivo = array[len(array)//2]

    esquerda = [x for x in array if x < pivo]
    meio = [x for x in array if x == pivo]
    direita = [x for x in array if x > pivo]

    return quick_sort(esquerda) + meio + quick_sort(direita)
