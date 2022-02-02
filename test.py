from Grafo import Grafo

grafo2 = Grafo(list("ABCD"), [
    ["A-B", 4],
    ["A-C", 1],
    ["C-D", 2],
])

print(grafo2.busca_em_profundidade("A", "D"))

grafo1 = Grafo(list("ABCD"), [
    ["A-B", 12],
    ["B-C", 15],
    ["A-C", 1],
    ["C-D", 2]
])

print(grafo1.busca_em_profundidade("A", "C"))