from graph import *

def main():
    g = Graph()
    g.add_edge(("a", "b"))
    g.add_edge(("b", "c"))
    g.add_edge(("c", "b"))
    
    print("The graph : ")
    print(g)

if __name__ == '__main__':
    main()
