#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        for i in range(idx, len(my_list) - 1):
            my_list[i] = my_list[i + 1]
        return my_list
