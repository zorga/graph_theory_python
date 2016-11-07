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

    def add_vertex(self, vertex):
        '''
        If the vertex 'vertex' is not in
        self.__graph_dict, a key 'vertex' with an empty
        list as a value is added to the dictionary.
        Otherwise nothing has to be done.
        '''
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def remove_vertex(self, vertex):
        '''
        Remove the vertex 'vertex' from the graph if present
        Do nothing otherwise
        '''
        if vertex in self.__graph_dict:
            del self.__graph_dict[vertex]

        # Also remove 'vertex' from all the other vertices neighbors list !
        for ver in self.__graph_dict.keys():
            if vertex in self.__graph_dict[ver]:
                # Remove ALL occurences of 'vertex' in neighbor list
                # Because there can be multiple edges between two vertices
                neigh_list = [x for x in self.__graph_dict[ver] if x != vertex]
                self.__graph_dict[ver] = neigh_list

    def add_edge(self, edge):
        '''
        assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        '''
        (vertex1, vertex2) = tuple(edge)

        # First add the corresponding vertex in the graph
        # If they are already in the graph, nothing happen
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Obviously, the two new vertices are neighbors
        self.__graph_dict[vertex1].append(vertex2)
        self.__graph_dict[vertex2].append(vertex1)

    def remove_edge(self, edge):
        '''
        remove the edge 'edge' from the graph
        warning : remove only one instance of 'edge' in the graph
        for example : removing edge ('a', 'b') between vertices 'a' and 'b'
        will only remove one such edge, but maybe there are multiple ones
        '''
        (vertex1, vertex2) = tuple(edge)
        self.__graph_dict[vertex1].remove(vertex2)
        self.__graph_dict[vertex2].remove(vertex1)

    def remove_all_edge(self, edge):
        '''
        remove all instances of the edge 'edge' in the graph
        '''
        (vertex1, vertex2) = tuple(edge)

        while vertex2 in self.__graph_dict[vertex1]:
            self.__graph_dict[vertex1].remove(vertex2)

        while vertex1 in self.__graph_dict[vertex2]:
            self.__graph_dict[vertex2].remove(vertex1)

    def is_adjacent(self, vertex1, vertex2):
        '''
        returns True if 'v1' and 'v2' are connected by an edge (minimum)
                False otherwise
        '''
        res = False

        if vertex1 == vertex2:
            res = True

        else:
            graph = self.__graph_dict
            res = (vertex1 in graph[vertex2] and vertex2 in graph[vertex1])

        return res

    def degree(self, vertex):
        '''
        returns the degree of the vertex 'vertex'. So, the number of edges
        that are connected to 'vertex', the loops count as two incidents edges
        '''
        return len(self.__graph_dict[vertex])

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

        for vertex in graph[start_vertex]:
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

        for vertex in graph[start_vertex]:
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
        queue.append(start_vertex)

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)

            for neighbor in self.__graph_dict[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return visited

    def __generate_edges(self):
        '''
        A static method generating the edges of the graph 'graph'.
        Edges are represented as sets with one (a loop back to the
        vertex) or two vertices
        '''
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
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
