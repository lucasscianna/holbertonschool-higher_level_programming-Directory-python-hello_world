#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = 0
    for i in my_list:
        count += 1
    if idx >= count:
        return None
    return my_list[idx]
    