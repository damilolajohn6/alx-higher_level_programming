#!/usr/bin/python3
'''
Module contains for checking the instance of an object
'''


def inherits_from(obj, a_class):
    '''
    Returns True if the object is exactly an instance of the specified class
    args:
    '''
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
