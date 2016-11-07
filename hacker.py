#!/usr/bin/python

'''
A python module to manipulate graphs
'''

from collections import deque

__author__ = "Nicolas Ooghe"


class Graph(object):
    '''
    A class to represent the Graph data structure.
    Undirected by default
    '''

    def __init__(self, directed=None, graph_dict=None):
        '''
        initialize a graph object
        If no dicttionary or None is given,
        an empty dictionary will be used
        '''
        if graph_dict is None:
            graph_dict = {}

        if directed is None:
            directed = False
        # Why setting the default values as 'None' :
        # http://effbot.org/zone/default-values.htm

        self.__directed = directed
        self.__graph_dict = graph_dict

    def directed(self):
        '''
        returns True if the graph is directed
                False otherwise
        '''
        return self.__directed

    def vertices(self):
        '''
        returns the vertices of a graph
        '''
        return list(self.__graph_dict.keys())

    def edges(self):
        '''
        returns the edges of a graph
        '''
        return self.__generate_edges()

    def add_vertex(self, label):
        '''
        If the vertex with label 'label' is not in
        self.__graph_dict, a key 'label' 
        with value : a Vertex object representing the vertex,
        is added into the dictionnary of the Graph
        '''
        ver = Vertex(label)
        if label not in self.__graph_dict:
            self.__graph_dict[label] = ver

    def get_vertex(self, label):
        '''
        returns the Vertex object with label 'label' if it is
        in the graph
        '''
        if label in self.__graph_dict.keys():
            return self.__graph_dict[label]
        else:
            print("No such Vertex !")
            return

    def remove_vertex(self, label):
        '''
        Remove the vertex 'vertex' from the graph if present
        Do nothing otherwise
        '''
        if label in self.__graph_dict:
            del self.__graph_dict[label]

        # Also remove 'vertex' from all the other vertices neighbors list !
        for ver in self.__graph_dict.keys():
            curr_vertex = self.__graph_dict[ver]
            if vertex in curr_vertex.neighbors():
                # Remove ALL occurences of 'vertex' in neighbor list
                # Because there can be multiple edges between two vertices
                neigh_list = [x for x in curr_vertex.neighbors() if x != vertex]
                self.__graph_dict[ver].set_neighbors(neigh_list)

    def add_edge(self, edge):
        '''
        assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        '''
        (label1, label2) = tuple(edge)

        # First add the corresponding vertex in the graph
        # If they are already in the graph, nothing happen
        self.add_vertex(label1)
        self.add_vertex(label2)

        # Obviously, the two new vertices are neighbors
        self.__graph_dict[label1].add_neighbor(label2)
        self.__graph_dict[label2].add_neighbor(label1)

    def remove_edge(self, edge):
        '''
        remove the edge 'edge' from the graph
        warning : remove only one instance of 'edge' in the graph
        for example : removing edge ('a', 'b') between vertices 'a' and 'b'
        will only remove one such edge, but maybe there are multiple ones
        '''
        (label1, label2) = tuple(edge)
        self.__graph_dict[label1].remove_neighbor(label2)
        self.__graph_dict[label2].remove_neighbor(label1)

    def remove_all_edge(self, edge):
        '''
        remove all instances of the edge 'edge' in the graph
        '''
        (label1, label2) = tuple(edge)

        while label2 in self.__graph_dict[label1].neighbors():
            self.__graph_dict[label1].remove_neighbor(label2)

        while label1 in self.__graph_dict[label2].neighbors():
            self.__graph_dict[label2].remove_neighbor(label1)

    def is_adjacent(self, label1, label2):
        '''
        returns True if 'v1' and 'v2' are connected by an edge (minimum)
                False otherwise
        '''
        res = False

        if label1 == label2:
            res = True

        else:
            graph = self.__graph_dict
            res = (label1 in graph[label2].neighbors() and label2 in graph[label1].neighbors())

        return res

    def degree(self, label):
        '''
        returns the degree of the vertex 'vertex'. So, the number of edges
        that are connected to 'vertex', the loops count as two incidents edges
        '''
        return len(self.__graph_dict[label].neighbors())

    def find_path(self, start_vertex, end_vertex, path=None):
        '''
        find a path from start_vertex to end_vertex in graph
        '''
        if path is None:
            path = []

        graph = self.__graph_dict
        path.append(start_vertex)

        if start_vertex == end_vertex:
            return path

        if start_vertex not in graph:
            return None

        if end_vertex not in graph:
            return None

        for vertex in graph[start_vertex].neighbors():
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        '''
        find all paths from start_vertex to end_vertex in graph
        '''
        if path is None:
            path = []

        graph = self.__graph_dict
        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return [path]

        if start_vertex not in graph:
            return []

        paths = []

        for vertex in graph[start_vertex].neighbors():
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for pat in extended_paths:
                    paths.append(pat)
            return paths

    def breadth_first_search(self, start_vertex):
        '''
        perform a BFS on the graph starting at vertex 'start_vertex'
        returns all vertices reachable from 'start_vertex'
        '''
        queue = deque()
        visited = set()
        self.__graph_dict[start_vertex].set_distance(0)
        queue.append(start_vertex)

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)

            for neighbor in self.__graph_dict[current].neighbors():
                if neighbor not in visited:
                    queue.append(neighbor)
                if self.__graph_dict[neighbor].distance() == 'INFINITY':
                    self.__graph_dict[neighbor].set_distance(self.__graph_dict[current].distance() + 1)
                    self.__graph_dict[neighbor].set_parent(current)

        return visited

    def __generate_edges(self):
        '''
        A static method generating the edges of the graph 'graph'.
        Edges are represented as sets with one (a loop back to the
        vertex) or two vertices
        '''
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex].neighbors():
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
                    # TODO: (issue #1) If there are more than one loops in the graph, it
                    # appends only one of them (bug to fix)
                    # Try to add the edge ('a', 'a') several times for example
                    # and print the graph to see the bug happening

        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "

        return res


class Vertex(object):
    '''
    Definition of the 'vertex' class
    '''

    def __init__(self, label, distance=None, parent=None):
        '''
        initialize a vertex object
        if no distance or None is given,
        the distance is set to 'INFINITY'
        parent should always be None at initialization
        ''' 
        if distance is None:
            distance = 'INFINITY'

        self.__label = label
        self.__distance = distance
        self.__parent = parent
        # Initialy empty neighbors list
        self.__neighbors = []

    def distance(self):
        '''
        return the distance of the vertex from root
        '''
        return self.__distance

    def set_distance(self, dist):
        '''
        update the distance attribute of the vertex
        '''
        self.__distance = dist

    def parent(self):
        '''
        return the parent of the vertex
        '''
        return self.__parent

    def set_parent(self, par):
        '''
        update the parent of the vertex
        '''
        self.__parent = par

    def label(self):
        '''
        return the label of the vertex
        '''
        return self.__label

    def add_neighbor(self, vertex):
        '''
        add the vertex object 'vertex' in the neighbor list
        of the current vertex
        '''
        self.__neighbors.append(vertex)

    def remove_neighbor(self, vertex):
        '''
        remove the vertex object 'vertex' from the neighbor list
        of the current vertex
        '''
        self.__neighbors.remove(vertex)

    def set_neighbors(self, neigh):
        '''
        update the neighbors attribute of the vertex object
        '''
        self.__neighbors = neigh

    def neighbors(self):
        '''
        return the list of neighbors of the current vertex
        '''
        return self.__neighbors

    def __str__(self):
        s = "Vertex : "
        s += "\nLabel : " + str(self.__label)
        s += "\nDistance : " + str(self.__distance)
        s += "\nParent : " + str(self.__parent)


def main():
    q = (int(raw_input().strip()))
    assert 1 <= q <= 10
    restab = []
    for i in range(q):
        n, m = raw_input().strip().split(' ')
        n, m = int(n), int(m)
        assert 2 <= n <= 1000
        assert 1 <= m <= ((n * (n - 1)) / 2)

        g = Graph()
        
        for j in range(m):
            u, v = raw_input().strip().split(' ')
            u, v = int(u), int(v)
            assert 1 <= u <= n
            assert 1 <= v <= n
            for k in range(1, n + 1):
                g.add_vertex(str(k))
            g.add_edge((str(u), str(v)))

        s = (int(raw_input().strip()))
        assert 1 <= s <= n
        g.breadth_first_search(str(s))
        res = ""
        nodes = []

        for v in g.vertices():
            nodes.append(int(v)) 
        nodes.sort() 

        for v in nodes:
            if str(v) != str(s):
                if g.get_vertex(str(v)).distance() == 'INFINITY':
                    res += "-1 "
                else:
                    val = g.get_vertex(str(v)).distance() * 6
                    res += str(val) + " "
        restab.append(res)

    for res in restab:
        print(res)


if __name__ == '__main__':
    main()
