#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    added_one = tuple_a[0] + tuple_b[0]
    added_two = tuple_a[1] + tuple_b[1]
    added = added_one, added_two
    return added
