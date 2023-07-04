#!/usr/bin/python3
def magic_string(my_list=[]):
    my_list.append("BestSchool") if len(my_list) == 0 else my_list.append(", BestSchool")
    return "".join(my_list)
