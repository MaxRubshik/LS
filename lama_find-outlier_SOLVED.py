import re

num = input('Enter number: ')
if not isinstance(num, str):
    num = str(num)

def f(exp, word):
    return bool(re.search(exp, word))

if f('8926\d{7}', num):
    print ('Megafon')
elif f('8952\d{7}', num):
    print ('Beeline')
elif f('8929\d{7}', num):
    print ('MTS')
else:
    print ('unknown')

