a = int(input('a:'))
op = input('operacja:')
b = int(input('b:'))

if op == '+':
    print('%s + %s = %s' % (a, b, (a + b)))
elif op == '-':
    print('%s - %s = %s' % (a, b, (a - b)))
elif op == '*':
    print('%s * %s = %s' % (a, b, (a * b)))
elif op == '/':
    print('%s / %s = %s' % (a, b, (a / b)))
