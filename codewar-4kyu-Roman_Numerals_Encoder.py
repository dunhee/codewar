'''
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.
'''

syb=list('IVXLCDM')
val=[1,5,10,50,100,500,1000]
D=dict(zip(val,syb))

def di(n):
    L=[n%10**(len(str(n))-i) for i in range(len(str(n)))]+[0]
    N=[L[i]-L[i+1] for i in range(len(L)-1)]
    return N
    
def solution(n):
    C=[]
    for i in di(n):
        for j in val[::-1]:
            if i==j:
                C.append(D[j])
                break
            elif i>j and i<1.8*j:
                C.append(D[j]+D[j/5]*int((i-j)/(j/5)))
                break
            elif i==1.8*j:
                C.append(D[j/5]+D[j*2])
                break
            elif i>=2*j and i<=3*j:
                C.append(D[j]*int(i/j))
                break
            elif i==4*j:
                C.append(D[j]+D[j*5])
                break
    return ''.join(C)