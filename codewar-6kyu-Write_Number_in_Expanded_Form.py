'''
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
'''

def expanded_form(n):
    L=[n%10**x-n%10**(x-1) for x in range(len(str(n)),0,-1)]
    M=[str(x) for x in L if x!=0]
    return ' + '.join(M)


'''
参考答案：
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x+'0'*(len(num)-y-1) for y,x in enumerate(num) if x!='0')
'''