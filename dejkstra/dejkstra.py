import random

__author__ = 'max'

class Node:
    COUNTER = 0

    def __init__(self):
        self.name = Node.COUNTER
        Node.COUNTER += 1

        self.mark = None
        self.connects = []

    def add_connect(self, value, node_to):
        if not isinstance(node_to, Node):
            raise TypeError
        self.connects.append((value, node_to))

    def is_last(self):
        for _, node in self.connects:
            if node.mark is None:
                return False
        return True

    def __str__(self):
        return '[%s]' % self.name


class Graph:
    def __init__(self):
        self.nodes = []

    def fill_nodes(self, amount):
        for i in range(amount):
            new_node = Node()
            self.nodes.append(new_node)

    def fill_random(self, amount):
        self.fill_nodes(amount)

        for node in self.nodes:
            for j in range(3):
                rand_value = random.randint(1, amount)
                node_to = random.randint(0, amount - 1)
                node.add_connect(rand_value * 10, self.nodes[node_to])

    def dejkstra_algorithm(self, initial):
        initial.mark = 0
        self._dejkstra_algorithm_rec(initial)

    def _dejkstra_algorithm_rec(self, current):
        for value, next_node in current.connects:
            if next_node.mark is None or next_node.mark > value + current.mark:
                next_node.mark = value + current.mark

        for value, next_node in current.connects:
            if not next_node.is_last():
                self._dejkstra_algorithm_rec(next_node)

    def __str__(self):
        result = ''
        for node in self.nodes:
            result += ('%s {%s} - ' % (node, node.mark))
            for value, next_node in node.connects:
                result += (' %s:%s, ' % (value, next_node))
            result += '\n'
        return result