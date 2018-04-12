""" 
The file is used to run any type of sort using this single file and its options
"""

from pigeonhole_sort import pigeonhole

def main():
    item = [int(x) for x in input("Please enter a list you would like to sort using PigeonSort: ").split()]
    print("Sorted order is : ", end = ' ')
    pigeonhole(item)
    for i in range(0, len(item)):
        print(item[i], end = ' ')

main()
