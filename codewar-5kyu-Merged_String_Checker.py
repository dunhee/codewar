'''
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 are in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears

('banana','ana','ban')
codewars can't be created from code and wasr
codewars is not a merge of cwdr and oeas

'''
def contain(s,p1,p2):
    return sorted(list(p1)+list(p2))==sorted(list(s))

def order(s,p):
    for x in p:
        if s.find(x)>=0:
            s=s[s.find(x)+1:]
        else: return False
    return True

def is_merge(s,p1,p2):
    return contain(s,p1,p2) and order(s,p1) and order(s,p2)

'''
参考答案：
def is_merge(s, part1, part2):
    if not part1:
      return s == part2
    if not part2:
      return s == part1
    if not s:
      return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
      return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
      return True
    return False
'''