# three.py env
'''
Mèxico 03-15-2023
Object3D module
Signed by alexistercero55@gmail.com

Authors:
- Lee Stemkoski  https://github.com/stemkoski
- Alexis Tercero https://github.com/AlexisTercero55
'''
import numpy as np
from OpenGL.GL import *
 
from mathutils import Matrix

class Object3D(object):
    '''# Object3D

The Object3D class represents a 3D object with a transformation matrix, parent-child relationships, and a name. It provides methods to add and remove child objects, compute the world transformation matrix, and filter and search its descendants.

## Attributes
* transform (Matrix): The transformation matrix of the object.
* parent (Object3D): The parent object of the current object, or `None` if it has no parent.
* children (list of Object3D): The list of child objects of the current object.
* name (str): The name of the object.

## Methods:
    add(child):
        Adds the specified child object to the list of children of the current object.
        Updates the child's parent reference accordingly.

    remove(child):
        Removes the specified child object from the list of children of the current object.
        Updates the child's parent reference accordingly.

    getWorldMatrix():
        Computes and returns the world transformation matrix of the current object,
        which is the product of the parent's world matrix and the current object's local matrix.
        Returns the local matrix if the current object has no parent.

    getDepthFirstList():
        Returns a list of descendants of the current object in depth-first order.
        The list is generated using a stack-based traversal algorithm.

    getObjectsByFilter(filterFunction=None):
        Returns a list of descendants of the current object that satisfy the specified filter function.
        The filter function should take an object as input and return a Boolean value.
        If no filter function is specified, returns the full list of descendants.

    getObjectByName(name):
        Returns the first descendant of the current object that has the specified name.
        Raises an error if no such object is found.

    '''

    def __init__(self)-> None:
        '''
        Initializes a new instance of the Object3D class.

        Attributes:
            transform (Matrix): The transformation matrix of the object.
            parent (Object3D): The parent object of the current object, or `None` if it has no parent.
            children (list of Object3D): The list of child objects of the current object.
            name (str): The name of the object.
        '''
        self.transform = Matrix()
        self.parent = None
        self.children = []
        self.name = ""
    
    def add(self, child: 'Object3D') -> None:
        '''
        Adds the specified child object to the list of children of the current object.
        Updates the child's parent reference accordingly.

        Args:
            child (Object3D): The child object to be added.
        '''
        # child instance of Object3D validation.
        if not isinstance(child, Object3D):
            raise ValueError("Child object must be an instance of Object3D.")
        # [c1,...,cn]
        self.children.append(child)
        # self ---> child
        child.parent = self
        
    def remove(self, child: 'Object3D')-> None:
        '''
        Removes the specified child object from the list of children of the current object.
        Updates the child's parent reference accordingly.

        Args:
            child (Object3D): The child object to be removed.
        '''
        if not isinstance(child, Object3D):
            raise ValueError("Child object must be an instance of Object3D.")
        self.children.remove(child)
        child.parent = None
        
    def getWorldMatrix(self)-> Matrix:
        '''
        Computes and returns the world transformation matrix of the current object,
        which is the product of the parent's world matrix and the current object's local matrix.
        Returns the local matrix if the current object has no parent.

        Returns:
            Matrix: The world transformation matrix of the current object.
        '''
         
        if self.parent == None: # *---> {}
            return self.transform.matrix
        else: # matrix product
            return self.parent.getWorldMatrix() @ self.transform.matrix
    
    # return a list of descendants in depth-first order
    def getDepthFirstList(self) -> list:
        '''
        Returns a list of descendants of the current object in depth-first order.
        The list is generated using a stack-based traversal algorithm.

        Returns:
            list of Object3D: The list of descendants in depth-first order.
        '''
        unvisitedList = [self]
        visitedList = []
        while len( unvisitedList ) > 0:
            item = unvisitedList.pop(0)
            visitedList.append(item)
            unvisitedList = item.children + unvisitedList
        return visitedList
        
    # return a list of descendants x with filterFunction(x) = True
    def getObjectsByFilter(self, filterFunction  = None)-> list:
        '''
        Returns a list of descendants of the current object that satisfy the specified filter function.
        The filter function should take an object as input and return a Boolean value.
        If no filter function is specified, returns the full list of descendants.

        Args:
            filterFunction (function, optional): 
            
                The filter function to be applied to the list of descendants.

                Defaults to None.

        Returns:
            list of Object3D: The list of descendants that satisfy the filter function.
        '''
        return list( filter( filterFunction, self.getDepthFirstList() ) )
        
    # return first descendent with name parameter matching given value
    def getObjectByName(self, name : str) -> 'Object3D' :
        '''
        Returns the first descendant of the current object with a name attribute matching the specified value.

        Args:
            name (str): The value to match against the name attribute.

        Returns:
            Object3D: The first descendant of the current object with a matching name attribute.

        Raises:
            IndexError: If no descendants are found with a matching name attribute.
        '''
        try:
            return self.getObjectsByFilter(lambda x: x.name == name)[0]
        except IndexError:
            raise IndexError(f"No descendants found with name attribute matching {name}")
        