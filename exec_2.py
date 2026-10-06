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

'''for string in ["arara", "banana", "A Santa no Natal", "Was it a car or a cat I saw"]:
    print(is_palidromo(string))'''

def factorial(int):
    if int == 0:
        return 1
    return int * factorial(int -1)

def factorial_iterativo(int):
    result = 1
    for numero in range(2, int + 1):
        result *= numero
    return result

'''for i_test in range(21):    
    print(f"O fatorial de {i_test} é {factorial_iterativo(i_test)}")'''

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

'''for fibonacci in [fibonacci_recursiva_i, fibonacci_iterativo, fibonacci_sequencia]:
    formato = "%H:%M:%S"
    agora = datetime.now()
    print(f"Iniciando registro às {agora.strftime(formato)}")
    print(fibonacci(40))
    fim = datetime.now()
    print(f"FInalizado às {fim.strftime("%H:%M:%S")}")
    print(f"Tempo de execução: {fim - agora}")'''

cache = {
    1:{"passos":0, "max_num":1}
} # {result: {"passos":0,"max_num":0}}

def collatz(num):
    caminho=[]
    result = num

    while result not in cache:
        caminho.append(result)

        if result % 2 == 0:
            result //= 2
        else:
            result = 3 * result + 1

    passos = cache[result]["passos"]
    max_num = cache[result]["max_num"]

    for n in reversed(caminho):
        passos += 1
        max_num = max(n, max_num)

        cache[n] = {
            "passos": passos,
            "max_num": max_num
        }

    return cache[num]["passos"], cache[num]["max_num"]

'''_num, _passos, _max = 1, 0, 1

for i in range(1, 1000000):
    passos, max_num = collatz(i)
    if passos > _passos:
        _num, _passos = i, passos
    _max = max(_max, max_num)

print(_num, _passos, _max)'''

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mdc_list(list:list):
    if len(list) == 0:
        raise ValueError("A lista não pode ser vazia")
    
    if len(list) == 1:
        return list[0]
    
    _list = []

    if len(list) % 2 == 0:
        for i in range(0, len(list), 2):
            _list.append(mdc(list[i], list[i + 1]))
        return mdc_list(_list)
    else:
        ultimo = list.copy().pop()
        return mdc(mdc_list(list), ultimo)

def mmc(a,b):
    return (a * b) // mdc(a, b)

'''
pares = [(12,8),(48,18),(100,75),(17,5),(0,5)]
_list_mdc = [12,8,48,18,100,75,17,5,0,5]

for par in pares:
    print(mdc(par[0], par[1]))
    print(mmc(par[0], par[1]))

print(mdc_list(_list_mdc))
    '''

class Pino:
    def __init__(self, nome:str, discos:list):
        self.nome = nome
        self.discos = discos

    def receber_disco(self, disco):
        self.discos.append(disco)

    def enviar_disco(self):
        if not self.discos:
            return 0

        return self.discos.pop()
    
def hanoi(n_discos, origem:Pino, auxiliar:Pino, destino:Pino): # Dificil (Nõa estava conseguindo entender a recursão)
    if n_discos == 1:
        destino.receber_disco(origem.enviar_disco())
        print(f"Mover disco de {origem.nome} para {destino.nome}")
        return
    
    hanoi(n_discos - 1, origem, destino, auxiliar)
    destino.receber_disco(origem.enviar_disco())
    print(f"Mover disco de {origem.nome} para {destino.nome}")

    hanoi(n_discos - 1, auxiliar, origem, destino)

'''n_discos = 5

pino_a = Pino("A", [d for d in reversed(range(1, n_discos+1))])
pino_b = Pino("B", [])
pino_c = Pino("C", [])

hanoi(n_discos, pino_a, pino_b, pino_c)'''

mapa = [
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1],
]

def n_ilhas(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])
    visitados = set()
    quant_ilhas = 0

    def visitar(i, j):
        if not (0 <= i < linhas and 0 <= j < colunas):
            return

        if mapa[i][j] == 0 or (i, j) in visitados:
            return

        visitados.add((i, j))

        visitar(i - 1, j)  # cima
        visitar(i + 1, j)  # baixo
        visitar(i, j - 1)  # esquerda
        visitar(i, j + 1)  # direita

    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == 1 and (i, j) not in visitados:
                quant_ilhas += 1
                visitar(i, j)

    return quant_ilhas

print(n_ilhas(mapa))