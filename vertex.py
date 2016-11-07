#!/usr/bin/python

'''
A python module defining the 'vertex' class to be used in the
'graph' class
'''

__author__ = 'Nicolas Ooghe'

class Vertex(object):
    '''
    Definition of the 'vertex' class
    '''

    def __init__(self, label, distance=None, parent=None):
        '''
        initialize a vertex object
        if no distance or None is given,
        the distance is set to 'INFINITY'
        parent should always be None at initialization
        ''' 
        if distance is None:
            distance = 'INFINITY'

        self.__label = label
        self.__distance = distance
        self.__parent = parent
        # Initialy empty neighbors list
        self.__neighbors = []

    def distance(self):
        '''
        return the distance of the vertex from root
        '''
        return self.__distance

    def set_distance(self, dist):
        '''
        update the distance attribute of the vertex
        '''
        self.__distance = dist

    def parent(self):
        '''
        return the parent of the vertex
        '''
        return self.__parent

    def set_parent(self, par):
        '''
        update the parent of the vertex
        '''
        self.__parent = par

    def label(self):
        '''
        return the label of the vertex
        '''
        return self.__label

    def add_neighbor(self, vertex):
        '''
        add the vertex object 'vertex' in the neighbor list
        of the current vertex
        '''
        self.__neighbors.append(vertex)

    def remove_neighbor(self, vertex):
        '''
        remove the vertex object 'vertex' from the neighbor list
        of the current vertex
        '''
        self.__neighbors.remove(vertex)

    def set_neighbors(self, neigh):
        '''
        update the neighbors attribute of the vertex object
        '''
        self.__neighbors = neigh

    def neighbors(self):
        '''
        return the list of neighbors of the current vertex
        '''
        return self.__neighbors

    def __str__(self):
        s = "Vertex : "
        s += "\nLabel : " + str(self.__label)
        s += "\nDistance : " + str(self.__distance)
        s += "\nParent : " + str(self.__parent)
