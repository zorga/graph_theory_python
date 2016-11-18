#!/usr/bin/python

from graph import *

def main():
    g = Graph()
    g.add_edge(('1', '2'))
    g.add_edge(('1', '3'))
    g.add_edge(('2', '4'))
    g.add_edge(('2', '5'))
    g.add_edge(('3', '6'))
    g.add_edge(('3', '7'))

    g.print_adjacency_matrix()
    g.dijkstra('1')

    print g

if __name__ == '__main__':
    main()
