history = [
 { "version": 1, "tests": "success" },
 { "version": 2, "tests": "success" },
 { "version": 3, "tests": "success" },
 { "version": 4, "tests": "failed" },
 { "version": 5, "tests": "failed" }
]


def search_bug(history):
    inicio = 0
    final = len(history) -1 

    while inicio <= final:
        meio = ((final - inicio) // 2 ) + inicio
        h_meio = history[meio]
        h_meio_1 = history[meio + 1]
        if h_meio["tests"] == "success" and h_meio_1["tests"] == "failed":
            return h_meio_1["version"]
        if h_meio["tests"] == "success":
            inicio += meio + 1
        else:
            final -= meio - inicio
        
#print(search_bug(history))

def search_in_system(system):
    visitados = []
    resultado = []
    pilha = ["checkout","pagamentos"]

    while len(pilha) > 0:
        ultimo = pilha.pop()
        if ultimo in visitados:
            continue
        visitados.append(ultimo)
        vizinhos = system[ultimo]
        for v in vizinhos:
            pilha.append(v)
            if v == "auth" or v in resultado:
                resultado.append(ultimo)
            

    return resultado

system = {
    "checkout": ["pagamentos"],
    "pagamentos": ["auth", "catalogo"],
    "catalogo":[],
    "auth":[]
}

print(search_in_system(system))
