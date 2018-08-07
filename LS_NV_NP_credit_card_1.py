num = input('Enter number: ')
if not isinstance(num, str):
    num = str(num)

def f(exp, word):
    return bool(re.search(exp, word))

if f('37\d{9}', num) or f('34\d{9}', num):
    print ('Amex')
elif f('6011\d{12}', num):
    print ('Discover')
elif f('4\d{12}', num) or f('4\d{15}', num):
    print ('VISA')
elif f('51\d{14}', num) or f('52\d{14}', num) or (
    f('53\d{14}', num) or f('54\d{14}', num)):
    print ('Mastercard')
else:
    print ('unknown')

