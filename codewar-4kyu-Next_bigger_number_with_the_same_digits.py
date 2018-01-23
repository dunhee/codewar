'''
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
(459853)==483559
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
'''

def next_bigger(n):
    L=list(str(n))
    for x in range(len(L)-1,-1,-1):
        if L[x:]!=sorted(L[x:],reverse=True):
            for y in range(len(L)-1,x,-1):
                if L[y]>L[x]:
                   L[y],L[x]=L[x],L[y]
                   L[x+1:]=sorted(L[x+1:])
                   return int(''.join(L))
    else:return -1



'''
参考答案：
def next_bigger(n):
    i, ss = n, sorted(str(n))

    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1;

    while True:
        i += 1;
        if sorted(str(i)) == ss and i != n:
            return i
'''

'''
参考答案：
def next_bigger(n):
    i, ss = n, sorted(str(n))

    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1;

    while True:
        i += 1;
        if sorted(str(i)) == ss and i != n:
            return i;
'''


'''
一种可用但较慢的思路：
def nb(n):
    from itertools import permutations
    l=[int(x) for x in list(str(n))]
    L=permutations(l,len(str(n)))
    A=[x for x in sorted(L) if list(x)>l]
    bg=int(''.join([str(x) for x in list(A[0])]))
    return bg if A[0] else -1
'''
