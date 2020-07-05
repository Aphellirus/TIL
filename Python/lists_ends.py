"""
This program takes a list of numbers and makes a new list of only the first and last elements of the given list
"""

random_list = [1,3,8,9,7,5,4,66,8,0,8,6,3,8]

def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
    
print (list_ends(random_list))
