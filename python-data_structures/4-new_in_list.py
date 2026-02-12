#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element without modifying original list."""
    new_list = my_list[:]
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list
