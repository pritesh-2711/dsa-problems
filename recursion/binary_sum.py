def binary_sum(S, start, stop):
    """A simple recursive function to sum a list of numbers"""
    if start >= stop:
        return 0                    # base case: no elements to sum     
    elif start == stop - 1:         # base case: only one element to sum
        return S[start]
    else:
        mid = (start + stop) // 2   # divide the list into two halves
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop) # recursive calls to sum the two halves
    
S = [i for i in range(1, 10000001)] # A list of numbers from 1 to 10 million
print(binary_sum(S, 0, len(S))) # Should print 50000005000000
    