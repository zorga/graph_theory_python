#!/usr/bin/python

def main():
    graph = {}
    graph['a'] = ['c']
    graph['b'] = ['c', 'e']
    graph['c'] = ['a', 'b', 'd', 'e']
    graph['d'] = ['c']
    graph['e'] = ['c', 'b']
    graph['f'] = []
    print(graph)
    print(generate_edges(graph))
    print(find_isolated_nodes(graph))


def generate_edges(graph):
    '''
    returns the list of all the edges in the graph
    '''
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    
    return edges


def find_isolated_nodes(graph):
    '''
    returns a list of isolated nodes
    '''
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    
    return isolated

if __name__ == '__main__':
    main()
