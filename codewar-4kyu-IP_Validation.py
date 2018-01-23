'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0..255 (included).

Input to the function is guaranteed to be a single string.

Examples
// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!
'''

def is_valid_IP(s):
    L=s.split('.')
    if len(L)!=4: return False
    try: M=[int(x) for x in L if int(x) in range(0,256)]
    except: return False
    else:
        if L!=[str(x) for x in M]: return False
    return True
    
    
'''
参考答案：
def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4
'''