
from graph import Graph


if __name__ == '__main__':
    graph = Graph()
    graph.fill_random(10)
    print graph

    initial = graph.nodes[5]
    graph.dejkstra_algorithm(initial)
    print graph
