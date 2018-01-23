'''
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.
'''

def di(n):
    s=0
    for i in range(1,n+1):
        if i<n/i and n%i==0:
            s+=i**2+(n/i)**2
        elif i==n/i:
            s+=i**2
        elif i>n/i:
            break
    if int(s**0.5)==s**0.5:
        return [n,int(s)]

def list_squared(m, n):
    return [di(n) for n in range(m,n+1) if di(n)!=None]

'''
参考答案：
from math import floor, sqrt, pow

def sum_squared_factors(n):
    s, res, i = 0, [], 1
    while (i <= floor(sqrt(n))):
        if (n % i == 0):
            s += i * i
            nf = n // i
            if (nf != i):
                s += nf * nf
        i += 1
    if (pow(int(sqrt(s)), 2) == s):
        res.append(n)
        res.append(s)
        return res
    else:
        return None
        
def list_squared(m, n):
    res, i = [], m
    while (i <= n):
        r = sum_squared_factors(i)
        if (r != None):
            res.append(r);
        i += 1
    return res
'''


'''
solution_inefficient:
def di(n):
    s=0
    for i in range(1,n+1):
        if n%i==0 and i<=n/i:
            if i==n/i:s+=i**2
            else:s+=i**2+(n/i)**2
    if s**0.5==int(s**0.5):
        return [n,int(s)]

def lsq(m,n):
    return [di(i) for i in range(m,n+1) if di(i)!=None]
'''

'''
solution_inefficient:
def di(n):
    s=sum([i**2 for i in range(1,n+1) if n%i==0])
    if int(s**0.5)==s**0.5: return [n,s]

def lsg(m,n):
    return [di(n) for n in range(m,n+1) if di(n)!=None]
'''