import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.connected_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        expected = Vertex('v3')
        expected.adjacent_to.append('v1')
        self.assertEqual(g.get_vertex('v3').adjacent_to, expected.adjacent_to)
        self.assertEqual(g.get_vertex('v12'), None)
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.connected_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
