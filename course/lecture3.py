""""Our first Python source file"""
from operator import floordiv, mod
def divide_exact(n, d):
    '''Return the quotient and remainder of dividing N by D.
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    '''
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x



#print("Quotient:",q)
#print('Remainder', r)

#windows中python lecture3.p(因为我配置的路径是python)，且要找到正确的路径
# 例如C:\Users\hehua\Desktop\cs61a1\course

#python -i 进入交互模式