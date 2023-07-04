#!/usr/bin/python3
def magic_string(my_list=["BestSchool"]):
    my_list.append(", BestSchool") if len(my_list) != 1 else my_list.append("")
    return "".join(my_list)
