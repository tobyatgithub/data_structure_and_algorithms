import sys
# import via absolute directory.
sys.path.append('/Users/toby/Documents/seattle-python-401d10/'
'data_structure_and_algorithms/data_structures/stack')

from stack import Stack


def multi_bracket_validation(input_string):
    """
    take a string as its only argument, and should return a
    boolean representing whether or not the brackets in the
    string are balanced. There are 3 types of brackets: (),
    [], and {}
    input: a string (str)
    output: T/F (boolean)
    """
    if not isinstance(input_string, str):
        print(f'please input str type, now {type(input_string)} given')
        raise(TypeError)

    open_Stack = Stack()
    open_samples = ['(','[','{']
    close_samples = [')',']','}']
    lookup = {
        '(':1,
        ')':1,
        '[':2,
        ']':2,
        '{':3,
        '}':3,
    }

    # if input is empty, return True as default,
    if input_string:
        for i in input_string:
            if i in open_samples:
                open_Stack.push(i)
            if i in close_samples:
                # we try to compare match
                tmp_open = open_Stack.pop()
                # if empty open_stack, direct False
                if not tmp_open:
                    return False
                # if doesn't mach, return False
                if lookup[i] != lookup[tmp_open.val]:
                    return False

    return True











    # clos_Stack = Stack()
    # clos_Stack = []
    #     # alright..this logic is a bit off..redo..
    #     # first, we collect each bracket into according stacks
    #     for i in input_string:
    #         if i in open_samples:
    #             open_Stack.push(i)
    #         if i in close_samples:
    #             clos_Stack.push(i)
    #             # clos_Stack.append(i)
    #     # check if the stacks are in same length
    #     if open_Stack._size != len(clos_Stack):
    #         return False

    #     # import pdb; pdb.set_trace()
    #     # match tops one by one
    #     for _ in range(open_Stack._size):
    #         tmp_open = open_Stack.pop().val
    #         tmp_clos = clos_Stack.pop().val
    #         # tmp_clos = clos_Stack.pop(-1)
    #         if lookup[tmp_clos] != lookup[tmp_open]:
    #             return False

    # return True
