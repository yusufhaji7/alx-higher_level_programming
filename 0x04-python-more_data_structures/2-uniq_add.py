#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        j = 0
        while j < i:
            if my_list[i] != my_list[j]:
                sum += my_list[i]
            j++
    return sum
