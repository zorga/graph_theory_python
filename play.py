#!/usr/bin/python

from graph import *

def main():
    print "Let's play with graphs !"
    
    g = Graph()
    print g
    g.add_edge(('a', 'b'))
    print g

if __name__ == '__main__':
    main()
