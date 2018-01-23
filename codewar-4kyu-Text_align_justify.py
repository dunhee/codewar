'''
Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 spaces).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

Have fun :)

test.expect_equals(justify('123 45 6', 7), '123 45\n6')
'''

#Step 1: Cut the string into desired lines.
def cut(s,n):
    if len(s)<=n:
        l=s
        return l,s
    else:
        if s[n-1]==' ':
            l=s[:n-1]
            s=s[n:]
        elif s[n]==' ':
            l=s[:n]
            s=s[n+1:]
        else:
            for i in range(n,0,-1):
                if s[i]==' ':
                    l=s[:i]
                    s=s[i+1:]
                    break
    return l,s

#Step 2: Pump up each line into desired length.
def pump(l,n):
    L=l.split(' ')
    blanks=n-len(l)
    if len(L)==1:return l
    else:
        while True:
            for i in range(0,len(L)-1):
                L[i]=L[i]+' '
                blanks-=1
                if blanks==0: break
            if blanks<0: break
        return ''.join(L)

#Step 3: Justify the whole string.
def justify(s,n):
    L=[]
    while True:
        l,s=cut(s,n)
        #print('l=',l)
        #print('s=',s)
        L.append('%s'%pump(l,n))
        #print('L=',L)
        if len(s)<=n: break
    L.append(s)
    return '\n'.join(L)

'''
参考答案：
def justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)
'''


'''
justify('Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.',15)
'''