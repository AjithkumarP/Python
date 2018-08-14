""" lambda basic with arg
x=lambda a:a+10
print(x(5))
"""

"""
Lambda with multiple arguments
x=lambda a,b: a+b
print(x(1,3))
"""
"""
    why use lambda 
def num_mul(n):
    return lambda a: a*n
myfun=num_mul(5)
print(myfun(5))    

"""