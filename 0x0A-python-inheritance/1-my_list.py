#!/usr/bin/python3
""" My list """


class MyList(list):
    """
    A custom list class that extends the built-in list
    class with additional functionality.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        This method creates a new list containing the elements of
        the current list, sorts it in ascending order, and
        then prints the sorted list.

        Example:
        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        """
        new_list = [i for i in self]
        sorted_list = sorted(new_list)
        print(sorted_list)
