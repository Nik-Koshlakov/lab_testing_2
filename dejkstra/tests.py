from graph import Graph, Node
import unittest

__author__ = 'nikita'


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node()

    def test_is_last_false(self):
        next_node = Node()
        self.node.connects.update({50: next_node})
        result = self.node.is_last()
        self.assertFalse(result)

    def test_is_last_true(self):
        next_node = Node()
        next_node.mark = 50
        self.node.connects.update({50: next_node})
        result = self.node.is_last()
        self.assertTrue(result)

    def test_is_last_empty(self):
        result = self.node.is_last()
        self.assertTrue(result)

    def test_add_connect_error(self):
        value = 50
        method = self.node.add_connect
        self.assertRaises(TypeError, method, args=(value, None))

    def test_add_connect_ok(self):
        value = 50
        self.node.add_connect(value, Node())
        self.assertTrue(self.node.connects[value])
        self.assertTrue(isinstance(self.node.connects[value], Node))

    def test_str_ok(self):
        self.node.name = 5
        string = str(self.node)
        self.assertEqual(string, '[5]')


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_fill_nodes_ok(self):
        amount = 3
        self.graph.fill_nodes(3)
        self.assertEqual(len(self.graph.nodes), amount)
        for node in self.graph.nodes:
            self.assertTrue(isinstance(node, Node))

    def test_dejkstra_algorithm_ok(self):
        self.graph.fill_nodes(4)

        # set connects
        self.graph.nodes[0].add_connect(10, self.graph.nodes[1])
        self.graph.nodes[1].add_connect(10, self.graph.nodes[2])
        self.graph.nodes[0].add_connect(15, self.graph.nodes[2])

        initial = self.graph.nodes[0]
        self.graph.dejkstra_algorithm(initial)

        # check marks
        self.assertEqual(self.graph.nodes[0].mark, 0)
        self.assertEqual(self.graph.nodes[1].mark, 10)
        self.assertEqual(self.graph.nodes[2].mark, 15)
        self.assertEqual(self.graph.nodes[3].mark, None)

    def test_str_empty(self):
        string = str(self.graph)
        self.assertEqual(string, '')

    def test_str_ok(self):
        self.graph.fill_nodes(1)
        string = str(self.graph)
        self.assertTrue(string)


if __name__ == '__main__':
    unittest.main()
