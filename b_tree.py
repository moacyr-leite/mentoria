
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.s_inf:Node = None
        self.s_sup:Node = None
    
    def add_son(self, valor):
        if valor > self.valor and not self.s_sup:
            self.s_sup = Node(valor)
        elif valor > self.valor and self.s_sup:
            self.s_sup.add_son(valor)
            return
        if valor < self.valor and not self.s_inf:
            self.s_inf = Node(valor)
        elif valor < self.valor and self.s_inf:
            self.s_inf.add_son(valor)
            return
        return "Não foi possivel adicionar son"

    def search_son(self, valor):
        if valor == self.valor:
            return True
        if valor > self.valor and self.s_sup:
            return self.s_sup.search_son(valor)
        if valor < self.valor and self.s_inf:
            return self.s_inf.search_son(valor)
        return False
    
    def in_order(self):
        return f"{f"{self.s_inf.in_order()}," if self.s_inf else ""}{self.valor}{f",{self.s_sup.in_order()}"if self.s_sup else ""}"
    
class BSTree:
    def __init__(self): 
        self.root:Node = None

    def add_son(self, valor):
        if not self.root:
            self.root = Node(valor)
            return
        
        self.root.add_son(valor)

    def search(self, valor):
        return self.root.search_son(valor)

    def in_order(self):
        return self.root.in_order()
