#!/usr/bin/python3
def search_replace(my_list, search, replace):

    newlist = [:]
    for i in range(len(my_list)):
        if newlist[i] == search:
            newlist[i] = replace
    return newlist