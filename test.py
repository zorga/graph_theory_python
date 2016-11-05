from graph import *

def main():
    gDict = {'a' : ['b', 'c'],
             'b' : ['a', 'd'],
             'e' : []
            }
    g = Graph(gDict)
    
    print("The graph : ")
    print(g)

if __name__ == '__main__':
    main()
