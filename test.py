#!/usr/bin/python

from graph import *

def main():
    gDict = {'a' : ['b', 'c'],
             'b' : ['a', 'd'],
             'c' : ['a'],
             'd' : ['b'],
             'e' : []
            }

    g = Graph(False, gDict)
    
    print("The graph : ")
    print(g)

if __name__ == '__main__':
    main()
