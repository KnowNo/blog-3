import math
def P(n, m):
    assert(n >= m)
    return math.factorial(n)/math.factorial(n-m)

def C(n, m):
    assert(n >= m)
    return P(n, m)/math.factorial(m)
    