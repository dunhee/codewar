'''
This is version 2 of my 'Write Number in Exanded Form' Kata.

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
expanded_form(0.04) # Should return '4/100'
'''

def expanded_form(n):
    P=str(n).split('.')
    Q1=[x+'0'*(len(P[0])-y-1) for y,x in enumerate(list(P[0])) if int(x)!=0]
    Q2=[x+'/1'+'0'*(y+1) for y,x in enumerate(list(P[1])) if int(x)!=0]
    return ' + '.join(Q1+Q2)