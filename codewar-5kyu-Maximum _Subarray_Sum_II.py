'''
Take a look to the kata Maximum Subarray Sum

In that kata (if you solved it), you had to give the maximum value of the elements of all the subarrays.

In this kata, we have a similar task but you have to find the sub-array or sub-arrays having this maximum value for their corresponding sums of elements. The wanted function:
Python and Ruby: ```find_subarr_maxsum()```// Javascript: ```findSubarrMaxSum()
find_subarr_maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [[4, -1, 2, 1], 6]
If in the solution we have two or more arrays having the maximum sum value, the result will have an array of arrays in the corresponding order of the array, from left to right.

find_subarr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4]) == [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]  # From left to right [4, -1, 2, 1] appears in the array before than [1, 2, -1, 4].
If the array does not have any sub-array with a positive sum of its terms, the function will return [[], 0].

See more cases in the Example Test Cases Window. Enjoy it!

Thanks to smile67 (Matthias Metzger from Germany for his important observations in the javascript version)
'''

#su([-2, 1, -3, 4, -1, 2, 1, -5, 4])
#su([4, -1, 2, 1, -40, 1, 2, -1, 4])

def su(L):
#def find_subarr_maxsum(L):
    M=[]
    N=[]
    s=0
    for i,x in enumerate(L):
        for j in range(i+1,len(L)+1):
            s = max(s,sum(L[i:j]))
            M.append([L[i:j],s])
    N=[l for [l,t] in M if sum(l)==s]
    return [N[0],s] if len(N)==1 else[N,s]