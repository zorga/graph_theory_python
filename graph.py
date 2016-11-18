#!/usr/bin/python

'''
A python module to manipulate graphs
'''

from collections import deque
from vertex import *

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
        self.__num_vertices = 0

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

    def num_vertices(self):
        '''
        returns the number of vertices in the graph
        '''
        return self.__num_vertices

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
            self.__num_vertices = self.__num_vertices + 1

    def get_vertex(self, label):
        '''
        returns the Vertex object with label 'label' if it is
        in the graph
        '''
        if label in self.__graph_dict.keys():
            return self.__graph_dict[label]
        else:
            print "No such Vertex in the graph !"
            return

    def remove_vertex(self, label):
        '''
        Remove the vertex 'vertex' from the graph if present
        Do nothing otherwise
        '''
        if label in self.__graph_dict:
            del self.__graph_dict[label]
            self.__num_vertices = self.__num_vertices - 1

            # Also remove 'vertex' from all the other vertices neighbors list !
            for ver in self.__graph_dict.keys():
                curr_vertex = self.__graph_dict[ver]
                if label in curr_vertex.neighbors():
                    # Remove ALL occurences of 'vertex' in neighbor list
                    # Because there can be multiple edges between two vertices
                    curr_vertex.remove_neighbor(label)

        else:
            print "No such Vertex in the graph !"
            return

    def add_edge(self, edge, cost=None):
        '''
        assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        'cost' is the weight of the edge, if None is given
        it will be set to "1" via the 'add_neighbor' method
        '''
        (label1, label2) = tuple(edge)

        # First add the corresponding vertex in the graph
        # If they are already in the graph, nothing happen
        self.add_vertex(label1)
        self.add_vertex(label2)

        # Obviously, the two new vertices are neighbors
        self.__graph_dict[label1].add_neighbor(label2, cost)
        self.__graph_dict[label2].add_neighbor(label1, cost)

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
                if self.__graph_dict[neighbor].distance() == sys.maxsize:
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
        res = "=" * 20
        res += "\nCurrent graph state : "
        res += "\nVertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nEdges: "
        for edge in self.__generate_edges():
            v1 = edge[0]
            v2 = edge[-1]
            edge_cost = self.get_vertex(v1).get_neighbor_cost(v2)
            edge_str = "[" + str(v1) + " --(" + str(edge_cost) + ")-- "+ str(v2) + "]"
            res += edge_str + " "
        res += "\n"
        res += "=" * 20
        res += "\n"

        return res
