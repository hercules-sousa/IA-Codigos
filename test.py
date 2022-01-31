from Grafo import Grafo

grafo1 = Grafo(list("ABCD"), [
    ["A-B", 12],
    ["B-C", 15],
    ["A-C", 1],
    ["C-D", 2]
])

print(grafo1)
print(grafo1.busca_em_profundidade("A", "D"))
