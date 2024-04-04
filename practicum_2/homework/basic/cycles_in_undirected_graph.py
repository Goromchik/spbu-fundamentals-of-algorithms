import networkx as nx


TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_w_cycles.edgelist",
]


def has_cycles(g: nx.Graph):
    cycles = nx.cycle_basis(g)
    #если метод возвращает непустой список, то цикл существует
    if len(cycles) > 0:
        print("Cycles found")
        return True
    else:
        return False
    pass


if __name__ == "__main__":
    for filename in TEST_GRAPH_FILES:
        # Load the graph
        G = nx.read_edgelist(f"D://algorithm//spbu-fundamentals-of-algorithms//practicum_2//homework//basic//{filename}", create_using=nx.Graph)
        # Output whether it has cycles
        print(f"Graph {filename} has cycles: {has_cycles(G)}")
