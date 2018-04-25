# Ryan Yu
# 04/21/2018
# python 2.7

import sys
# ast library used for string parsing
import ast
from collections import deque


'''
    isatom(list): this function takes one parameter,
    a variable of any datatype. This functino will 
    return false if the input parameter is a list datatype. 
    It will return true is the input parameter is not a list,
    i.e. an 'atom'.
    ex: 
        - [1, 2, 3] is a list and will return false.
        - 1 is an atom and will return true. 
'''
def isatom(item):
    return not(type(item) is list)

'''
    iterflatten(list): this function takes one parameter,
    a list. It will perform a flattening operation, turning
    any internal lists to single elements. It does this 
    using a stack like data structure to do a depth first search 
    through the list. This function will return a list containing the 
    flattened input list. 
'''
def iterflatten(list):
    stack = deque(list)
    output = []

    while len(stack) != 0:
        temp = stack.popleft()
        if isatom(temp):
            output.append(temp)
        else:
            # if the next item in the stack is another list
            # that needs to be flattened, push it to the
            # front of the stack, maintaining the order
            # of the items in the sub-list.
            for i in range(len(temp)-1, -1, -1):
                stack.appendleft(temp[i])

    return output


def main():
    text = raw_input("Enter a list, with each element separated by commas: ")

    # ast.literal_eval will validate and evaluate the user input
    # and store it as a list
    # user input must come as a comma separated string
    # ex: [1, 2, 3] is correct input, but [1 2 3] is not.
    try:
        userlist = ast.literal_eval(text)
    except:
        print("Unable to parse input.")
        sys.exit()

    finalOutput = iterflatten(userlist)
    print "final output: ", finalOutput


main()


