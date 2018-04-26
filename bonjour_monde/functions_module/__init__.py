"""
Example Functions
"""


def get_foo():
    """
    Gets the word foo.
    
    :return: str, the word 'foo' 
    """

    return 'foo'


def print_bar():
    """
    Prints the work bar

    :return: None 
    """

    print('bar')


__all__ = sorted(['get_foo', 'print_bar'])
