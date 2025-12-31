from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.dgraph = {}
        with open(filename, 'r') as f:
            for line in f:
                vertices = line.split()
                if len(vertices) == 2:
                    self.add_vertex(vertices[0])
                    self.add_vertex(vertices[1])
                    self.add_edge(vertices[0], vertices[1])

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.dgraph:
            self.dgraph[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.dgraph[v1].adjacent_to.append(v2)
        self.dgraph[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key in self.dgraph:
            return self.dgraph[key]
        else:
            return None

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        keys = self.dgraph.keys()
        ordered_keys = sorted(keys)
        return ordered_keys

    def connected_components(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        #This method MUST use Depth First Search logic!
        list_of_components = []
        seen = set()
        vertices = self.get_vertices()
        for vertex in vertices:
            if vertex not in seen:
                component = self.connected_helper(vertex, seen)
                list_of_components.append(sorted(component))
        return sorted(list_of_components, key=lambda x: x[0])
    def connected_helper(self, start_vertex, seen):
        stack = Stack(len(self.get_vertices()))
        stack.push(start_vertex)
        connected = []
        seen.add(start_vertex)
        while not stack.is_empty():
            current = stack.pop()
            connected.append(current)
            for next_vertex in self.dgraph[current].adjacent_to:
                if next_vertex not in seen:
                    stack.push(next_vertex)
                    seen.add(next_vertex)
        return connected

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        vertices = self.get_vertices()
        queue = Queue(len(vertices))
        colored = {}
        for vertex in vertices:
            if vertex not in colored:
                if not self.bipartite_helper(vertex, queue, colored):
                    return False
        return True

    def bipartite_helper(self, root, queue, colored):
        '''Helper function to perform BFS and check bipartiteness.'''
        queue.enqueue(root)
        colored[root] = 'purple'
        while not queue.is_empty():
            current = queue.dequeue()
            current_color = colored[current]
            neighbor_color = 'red' if current_color == 'purple' else 'purple'
            for neighbor in self.dgraph[current].adjacent_to:
                if neighbor not in colored:
                    colored[neighbor] = neighbor_color
                    queue.enqueue(neighbor)
                elif colored[neighbor] != neighbor_color:
                    return False
        return True