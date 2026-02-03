from typing import Literal
from pydantic import BaseModel

class RulerScale(BaseModel):
    n : Literal[10, 15, 30, 60, 100]

def design_ruler(n: int):
    """ Design a english ruler using recursion"""
    if n==0:
        print("---- 0")
    
    elif n%10==0:
        print("---- ",n)
        design_ruler(n-1)

    elif n%5==0:
        print("-- ",n)
        design_ruler(n-1)

    else:
        print("-")
        design_ruler(n-1)
    
    pass
