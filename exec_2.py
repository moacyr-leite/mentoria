from datetime import datetime

def is_palidromo(text:str):
    string = "".join(text.lower().split(" "))
    inicio = 0
    final = len(string) - 1

    for c in range(final):
        if string[inicio] == string[final]:
            inicio += 1
            final -= 1
            continue
        else:
            return False
    return True

#for string in ["arara", "banana", "A Santa no Natal", "Was it a car or a cat I saw"]:
#    print(is_palidromo(string))

def factorial(int):
    if int == 0:
        return 1
    return int * factorial(int -1)

def factorial_iterativo(int):
    result = 1
    for numero in range(2, int + 1):
        result *= numero
    return result

#for i_test in range(21):    
#    print(f"O fatorial de {i_test} é {factorial_iterativo(i_test)}")

def fibonacci_recursiva_i(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursiva_i(n-1) + fibonacci_recursiva_i(n-2)

def fibonacci_cache(n):
    cache = {
        0: 0,
        1: 1
    } # Não tenho certeza de como implementar o cache. Pesquisar mais tarde
    if n in cache.keys():
        return cache[n]
    
    return

def fibonacci_iterativo(n):
    result = 0
    a = 0
    b = 1
    for num in range(n-1):
        c = a+b
        a, b = b, c

    return b

def fibonacci_sequencia(n):
    sequencia = []
    for num in range(n+1):
        sequencia.append(fibonacci_iterativo(num))
    return sequencia

#for fibonacci in [fibonacci_recursiva_i, fibonacci_iterativo, fibonacci_sequencia]:
#    formato = "%H:%M:%S"
#    agora = datetime.now()
#    print(f"Iniciando registro às {agora.strftime(formato)}")
#    print(fibonacci(40))
#    fim = datetime.now()
#    print(f"FInalizado às {fim.strftime("%H:%M:%S")}")
#    print(f"Tempo de execução: {fim - agora}")

def collatz(num):
    pasos = 0
    max_num = 1
    sequencia = [num]
    result = num
    cache = {} # {result: {"sequencia":[],"pasos":0,"max_num":0}} # Melhorar Cache
    while result != 1:
        if result in cache.keys():
            sequencia.append(cache[result]["sequencia"])
            pasos += cache[result]["pasos"]
            max_num = cache[result]["max_num"] if max_num < cache[result]["max_num"] else max_num

            return sequencia, pasos, max_num
        else:
            cache[result] = {}
            cache[result]["sequencia"] = sequencia
            cache[result]["pasos"] = pasos
            cache[result]["max_num"] = max_num
        
        if result > max_num:
            max_num = int(result)
        if result % 2 == 0:
            result = result / 2
            sequencia.append(int(result))
            pasos += 1
            continue
        if result % 2 == 1:
            result = (result * 3) + 1
            sequencia.append(int(result))
            pasos += 1
            continue 
    
    return sequencia, pasos, max_num

_num, _pasos = 1, 0

for i in range(1, 1000000):
    sequencia, pasos, max_num = collatz(27)
    print(f"{i}: {pasos} pasos")
    if pasos > _pasos:
        _num, _pasos = i, pasos

print(_num, _pasos)