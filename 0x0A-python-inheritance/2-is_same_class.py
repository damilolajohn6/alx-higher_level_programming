#!/usr/bin/python3
'''
Module contains for checking the instance of an object
'''


def is_same_class(obj, a_class):
    '''
    Returns True if the object is exactly an instance of the specified class
    args:
    Returns:
        boolean: True if object is exactly an instance of the specified class
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
