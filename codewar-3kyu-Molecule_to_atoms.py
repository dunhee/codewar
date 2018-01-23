'''
For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

'''

'''
test:
C6H12O6
m2a('Pd[P(C6H5)3]4')
As2{Be4C5[BCo3(CO2)3]2}4Cu5
m2a('{[Co(NH3)4(OH)2]3Co}(SO4)3')
m2a('Fe(C5H5)2')
'''

#Step 1: Identify elements such as "Fe" from "N", and '12' from '1','2'
def comb(S):
    S1=[]
    for i,x in enumerate(S):
        if i<len(S)-1 and S[i].isupper()==True and S[i+1].islower()==True:
            S1.append(''.join(S[i:i+2]))
        elif S[i].islower()==True:
            continue
        elif S[i].isdigit()==True and S[i-1].isdigit()==True:
            continue
        elif i<len(S)-1 and S[i].isdigit()==True:
            t=[S[i]]
            for j in range(i+1,len(S)):
                if S[j].isdigit()==False:break
                else:
                    t.append(S[j])
            S1.append(''.join(t))
        else:
            S1.append(x)
    return S1
    
#Step 2: Get a dictionary of elements.
def elmt(S):
    elmts=[x for x in comb(S) if x.isalpha()==True]
    return {x:0 for x in elmts}

#Step 3: Pump up elements such as 'O3' into 'OOO'
def pmp(S):
    S1=[]
    for i,x in enumerate(S):
        if i<len(S)-1 and S[i].isalpha==True and S[i+1]==S[i]:
            continue
        elif i<len(S)-1 and x.isalpha()==True and S[i+1].isdigit()==True:
            S1.append([S[i]]*int(S[i+1]))
        else:
            S1.append(x)
    return S1

#Step 4: Expand by interpreting brackets
def brk(l,r,S):
    for i,x in enumerate(S):
        if isinstance(x,list)==False:
            if x.isdigit()==True and S[i-1]==r:
                for j in range(i-2,-1,-1):
                    if S[j]==l:break
                    elif isinstance(S[j],list)==True and ''.join(S[j]).isalpha()==True:
                        S[j]=S[j]*int(S[i])
                    elif S[j].isalpha()==True:
                        S[j]=[S[j]]*int(S[i])
    return S

#Step 5: Count elements after 3 types of brackets interpreted.
def parse_molecule(s):
    S=list(s)
    D=elmt(S)
    S0=pmp(comb(S))
    S1=brk('(',')',S0)
    S2=brk('[',']',S1)
    S3=brk('{','}',S2)
    for x in S3:
        for y in list(D.keys()):
            if isinstance(x,list):
                D[y]+=x.count(y)
            elif x.isalpha() and y==x:
                D[y]+=1
    return D
    
    
'''
参考答案：
from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts
'''