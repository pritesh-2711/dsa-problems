def reverse(sequence, start, stop):
    """ Reverse a list using recursion.
    Args :
    sequence : List to be reversed
    start : initial index
    stop : last index

    Output :
    reversed_sequence : List 
    """

    if start < stop -1:
        sequence[start], sequence[stop-1] = sequence[stop-1], sequence[start]
        reverse(sequence, start+1, stop-1)

    # else condition is not required as len(2) means swap, len(1) means return same, len(0) means Not possible 
    return sequence

# S = [1,2,3,4,5]
# S=[1,2]
# S=[1]
# S=[]

# print(reverse(S, 0, len(S)))