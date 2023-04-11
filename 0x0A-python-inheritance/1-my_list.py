#!/usr/bin/python3
"""MyList module"""


class MyList(list):
""" Prints the list sorted in ascending order. """
    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
