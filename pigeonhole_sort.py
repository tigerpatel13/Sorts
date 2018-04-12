""" 
An attempt to create a repository of all types of sorts provided at a standardized location for use in Python. 
"""

"""
This specific file contains the source code for the pigeon hole sort algorithm.
"""
def pigeonhole(item):
    #Gather the length of the list
    item_min = min(item);
    item_max = max(item);
    item_length = item_max - item_min + 1;

    #List of PigeonHoles
    holes = [0] * item_length;

    #Populating the PigeonHoles
    for i in item:
        assert type(i) is int, "Values must be integers"
        holes[i - item_min] += 1

    #Creating an array of the result 
    j = 0;
    for count in range(item_length):
        while holes[count] > 0:
            holes[count] -= 1
            item[j] = count + item_min
            j += 1
