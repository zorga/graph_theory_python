#!/usr/bin/python

'''
A python module defining the 'vertex' class to be used in the
'graph' class
'''

__author__ = 'Nicolas Ooghe'

class vertex(object):
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

        self.__distance = distance
        self.__label = label
        self.__parent = parent

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

    def __str__(self):
        s = "Vertex : "
        s += "\nLabel : " + str(self.__label)
        s += "\nDistance : " + str(self.__distance)
        s += "\nParent : " + str(self.__parent)
