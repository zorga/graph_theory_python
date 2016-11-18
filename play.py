#!/usr/bin/python

from graph import *

def main():
    print "Let's play with graphs !"
    
    g = Graph()
    print g

    print "add edge A -- B"
    g.add_edge(('A', 'B'))
    print g

    print "add edge A -- B"
    g.add_edge(('A', 'B'))
    print g

    print "add edge D -- C"
    g.add_edge(('D', 'C'))
    print g

    print "remove vertex C"
    g.remove_vertex('C')
    print g

    print "Are A and B adjacent ? : " + str(g.is_adjacent('A', 'B'))
    print "Are A and D adjacent ? : " + str(g.is_adjacent('A', 'D'))

    print "\nadd edge X -- Y"
    g.add_edge(('X', 'Y')) 
    print g

    print "add edge X -- Z"
    g.add_edge(('X', 'Z'))
    print g 

    print "add edge X -- V"
    g.add_edge(('X', 'V'))
    print g 

    print "Neighbors of X :"
    print str(g.get_vertex('X').neighbors())
    print "\n"
    
    print "remove vertex V\n"
    g.remove_vertex('V')
    print "Neighbors of X : "
    print str(g.get_vertex('X').neighbors())
    print g

    print "add three edges X -- Z"
    g.add_edge(('X', 'Z'))
    g.add_edge(('X', 'Z'))
    g.add_edge(('X', 'Z'))
    print g
    
    print "remove an X -- Z edge"
    g.remove_edge(('X', 'Z'))
    print g
     
    print "remove an X -- Z edge"
    g.remove_edge(('X', 'Z'))
    print g

    print "remove an X -- Z edge"
    g.remove_edge(('X', 'Z'))
    print g

    print "remove an X -- Z edge"
    g.remove_edge(('X', 'Z'))
    print g

    print "remove an X -- Z edge"
    g.remove_edge(('X', 'Z'))
    print g
    
    print "add edge G -- H"
    g.add_edge(('G', 'H'))
    print g
    print "Neighbors of G : "
    print str(g.get_vertex('G').neighbors())
    print "Neighbors of H : "
    print str(g.get_vertex('H').neighbors())

    print "add edge G -- H"
    g.add_edge(('G', 'H'))
    print g
    print "Neighbors of G : "
    print str(g.get_vertex('G').neighbors())
    print "Neighbors of H : "
    print str(g.get_vertex('H').neighbors())
    
    print "remove edge G -- H"
    g.remove_edge(('G', 'H'))
    print g
    print "Neighbors of G : "
    print str(g.get_vertex('G').neighbors())
    print "Neighbors of H : "
    print str(g.get_vertex('H').neighbors())

    print "remove edge G -- H"
    g.remove_edge(('G', 'H'))
    print g
    print "Neighbors of G : "
    print str(g.get_vertex('G').neighbors())
    print "Neighbors of H : "

    print str(g.get_vertex('H').neighbors())
    print "remove edge G -- H"
    g.remove_edge(('G', 'H'))
    print g
    print "Neighbors of G : "
    print str(g.get_vertex('G').neighbors())
    print "Neighbors of H : "
    print str(g.get_vertex('H').neighbors())

if __name__ == '__main__':
    main()
