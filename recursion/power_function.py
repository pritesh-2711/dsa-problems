import time

class Power:
    """ A class with different methods to calculate power 'n' of any non-negative number 'x'. Provides runtime for each method. """

    def use_loops(x:int, n:int):
        """ Use loops to solve the problem"""
        result = 1
        while n>0:
            result = result * x
            n -= 1
        return result
    
    def use_basic_recursion(x:int, n:int):
        """ Use recursion fn(x) * fn(x-1) logic"""
        if n==0:
            return 1
        else:
            return x * Power.use_basic_recursion(x, n-1)

    def use_even_odd_property(x:int, n:int):
        """ Squaring property of exponential functions are used :
        x^(n) = (x^(n))^2     ==>  x^(n)     -------------> for even 'n'
        x^(n) = (x^(n+1)/2)^2 ==>  x * x^(n) -------------> for odd 'n'
        """
        if n==0:
            return 1
        else:
            half_result = Power.use_even_odd_property(x, n//2) # Doing a floor division by 2
            result = half_result * half_result # taking square to compensate for power division by 2

            # Check for even/odd case
            if n%2==1:
                result = x * result # Odd 'n'

            return result

# runtime_a = time.time()
# print(Power.use_loops(202551,17))
# runtime_b = time.time()
# print(f"Runtime : {(runtime_b - runtime_a)} sec")

# runtime_a = time.time()
# Power.use_basic_recursion(202551,17)
# runtime_b = time.time()
# print(f"Runtime : {(runtime_b - runtime_a)} sec")

# runtime_a = time.time()
# Power.use_even_odd_property(202551,17)
# runtime_b = time.time()
# print(f"Runtime : {(runtime_b - runtime_a)} sec")
