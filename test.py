from graph import *

def main():
    g = Graph()
    #g.add_edge({"a", "b"})
    #g.add_edge({"b", "c"})
    g.add_edge(["a", "a"])
    path = g.find_path("a", "c")
    print(g)
    print(path)

if __name__ == '__main__':
    main()
