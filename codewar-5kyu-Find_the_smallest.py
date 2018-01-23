'''
You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another place in the number.

Doing so, find the smallest number you can get.

#Task: Return an array or a tuple or a string depending on the language (see "Sample Tests") with

1) the smallest number you got
2) the index i of the digit d you took, i as small as possible
3) the index j (as small as possible) where you insert this digit d to have the smallest number.
Example:

smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

smallest(209917) --> [29917, 0, 1] or ...

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
index `i` in [29917, 0, 1].
29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.

smallest(1000000) --> [1, 0, 6] or ...
Note
Have a look at "Sample Tests" to see the input and output in each language
'''

def smallest(n):
    L=[n,0,0]
    S=list(str(n))
    for i in range(len(S)):
        for j in range(len(S)):
            if i==j:continue
            elif i<j:
                S1=S[:i]+S[i+1:j+1]+[S[i]]+S[j+1:]
            else:
                S1=S[:j]+[S[i]]+S[j:i]+S[i+1:]
            L=min([int(''.join(S1)),i,j],L)
    return L

'''
参考答案：
def smallest(n):
    s, mem = str(n), [-1, -1, -1]
    tmp, l = s, len(s)
    for i in range(l):
        c = s[i]
        str1 = s[:i] + s[i + 1:]
        for j in range(0, l):
            str2 = str1[:j] + c + str1[j:]
            if (str2 < tmp):
                tmp = str2
                mem = [int(tmp), i, j]
    if (mem[0] == -1): mem = [n, 0, 0]
    return mem
'''