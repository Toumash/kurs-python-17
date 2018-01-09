y = 1

while y <= 10:
    print(y)
    y += 2

print('xd')


def powitaj(imie):
    print('Witaj, %s :) ' % imie)


# f(x) = 2*x + 3
# f(5) + 3 = 16
def f(x):
    return 2 * x + 3


powitaj('Mariuszu')
powitaj('Tomaszu')

print(f(16))

'''
silnia(3)=3*silnia(3-1)
                2 * silnia(2-1)
                        1
'''


def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n - 1)


print('silnia z 3 = %s ' % silnia(3))
print('silnia z 5 = %s ' % silnia(5))
print('silnia z 100 = %s ' % silnia(100))
print('silnia z 200 = %s ' % silnia(200))
silniaZ900 = len(str(silnia(900)))
# length == len w pythonie
print('silnia z 255 = %s ' % silniaZ900)
