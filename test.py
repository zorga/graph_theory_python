from graph import *

def main():
    g = Graph()
    #g.add_edge(["a", "b"])
    #g.add_edge(["o", "p"])
    #g.add_edge(["b", "p"])
    #path = g.find_path("a", "p")
    #path2 = g.find_path("a", "o")
    g.add_edge(("a", "b"))
    g.add_edge(("b", "c"))
    g.add_edge(("c", "d"))
    g.add_edge(("x", "y"))
    g.add_edge(("a", "a"))
    g.add_edge(("a", "a"))
    g.add_edge(("c", "x"))
    
    g.add_edge(("a", "y"))
    
    
    #path = g.find_path("a", "c")
    #path2 = g.find_path("a", "d")
    #path3 = g.find_path("c", "d")
    path4 = g.find_path("a", "y")

    allpath = g.find_all_paths("a", "y")

    #print("path from a to c : " + str(path))
    #print("path from a to d : " + str(path2))
    #print("path from c to d : " + str(path3))
    print("\npath from a to y : ")
    print(path4)
    print("\nall paths from a to y : ")
    print(allpath)

    print("\nThe graph : ")
    print(g)

if __name__ == '__main__':
    main()
