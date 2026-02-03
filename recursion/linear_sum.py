from typing import List

def linear_sum(S : List[int], n : int):
    """Recursively calculate the sum of first n elements of list"""
    if n==0:
        return 0
    else:
        return linear_sum(S=S, n=n-1) + S[n-1]
    
# print(linear_sum([1,2,3,4,5], 3))