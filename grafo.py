class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.conect = []
        
    def __str__(self):
        return f"{self.nome}"
    
    def __repr__(self):
        return f"{self.nome}"

class Aresta:
    def __init__(self, v_nome_1, v_nome_2, peso = 0, direction = ""):
        """
        direction
        1: Unidirecional 
        2: Bidirecional
        3: Unidirecional Inversa 
        """
        self.v_nome_1 = v_nome_1
        self.v_nome_2 = v_nome_2
        self.peso = peso
        self.direction = direction

class Grafo:
    def __init__(self):
        self.vertices:list[Vertice] = []
        self.arestas:list[Aresta] = []
        
    def add_vertice(self, vertice:Vertice):
        self.vertices.append(vertice)

    def get_vertice(self, a_nome) -> Vertice:
        for v in range(len(self.vertices) -1):
            if self.vertices[v].nome == a_nome:
                return self.vertices[v]

    def _connectar(self, v_nome_1, v_nome_2):
            self.get_vertice(v_nome_1).conect.append(v_nome_2)

    def add_aresta(self, aresta:Aresta):
        if aresta.direction == 1:
            self._connectar(aresta.v_nome_1, aresta.v_nome_2)

        if aresta.direction == 2:
            self._connectar(aresta.v_nome_1, aresta.v_nome_2)
            self._connectar(aresta.v_nome_2, aresta.v_nome_1)

        if aresta.direction == 3:
            self._connectar(aresta.v_nome_2, aresta.v_nome_1)

        self.arestas.append(aresta)

    def get_aresta(self, v_nome_1, v_nome_2):
        for a in range(len(self.arestas) -1):
            if self.arestas[a].v_nome_1 == v_nome_1 and self.arestas[a].v_nome_2 == v_nome_2:
                return self.arestas[a]
                
    def get_vizinhos(self, v_nome):
            return self.get_vertice(v_nome).conect

list_adjacencia = [
    ["A", "B", "C", "D", "E", "F"],
    [
        [("B"), ("D"), ("F")] # A
        [("A"), ("C"), ("E")] # B
        [("B"), ("D"), ("E")] # C
        [("A"), ("C"), ("F")] # D
        [("B"), ("C"), ("F")] # E
        [("A"), ("D"), ("E")] # F
    ]
]
grafo = Grafo()

for e in list_adjacencia[0]:
    grafo.add_vertice(Vertice(e))

print(grafo.vertices)
