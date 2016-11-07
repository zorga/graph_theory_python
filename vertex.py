#!/usr/bin/python

'''
A python module defining the 'vertex' class to be used in the
'graph' class
'''

__author__ = 'Nicolas Ooghe'

import sys

class Vertex(object):
    '''
    Definition of the 'vertex' class
    '''

    def __init__(self, label, distance=None, parent=None):
        '''
        initialize a vertex object
        if no distance or None is given,
        the distance is set to sys.maxsize 
        parent should always be None at initialization
        ''' 
        if distance is None:
            distance = sys.maxsize

        self.__label = label
        self.__distance = distance
        self.__previous = None 
        self.__parent = parent
        # Initialy empty neighbors list
        # For each key in the neighbor dict, the value is the weight
        # of the edge linking the present vertex to this neighbor
        self.__neighbors = {}

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

    def previous(self):
        '''
        returns the 'previous' attr of the instance of Vertex
        '''
        return self.__previous

    def set_previous(self, prev):
        '''
        updates the 'previous' attribute of the instance of vertex
        '''
        self.__previous = prev

    def label(self):
        '''
        return the label of the vertex
        '''
        return self.__label

    def add_neighbor(self, vertex, weight=None):
        '''
        add the vertex object 'vertex' in the neighbor dict
        of the current vertex
        weight is the cost of the edge linked to this neighbor
        '''
        if weight is None:
            weight = 1
        if vertex not in self.__neighbors.keys():
            self.__neighbors[vertex] = weight

    def remove_neighbor(self, vertex):
        '''
        remove the vertex object 'vertex' from the neighbor list
        of the current vertex
        '''
        if vertex in self.__neighbors.keys():
            del self.__neighbors[vertex]

    def set_neighbors(self, neigh):
        '''
        update the neighbors attribute of the vertex object
        '''
        self.__neighbors = neigh

    def neighbors(self):
        '''
        return the dict of neighbors of the current vertex
        '''
        return self.__neighbors

    def __str__(self):
        s = "Vertex : "
        s += "\nLabel : " + str(self.__label)
        s += "\nDistance : " + str(self.__distance)
        s += "\nParent : " + str(self.__parent)
