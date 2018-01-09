listaList = [
    ['Mariusz', 'Czerkies', 'mczerkies@wsbcode.pl'],
    ['Tomasz', 'Dluski', 'tomasz.dluski@studentpartner.com']
]

print(listaList)
listaList.append(['Szymon', 'Zaborowski', ''])
print(listaList[1][2])

'''
Dowolny tekst na 
jakakolwiek 
ilosc
wierszy
'''

listaSlownikow = [
    {
        'imie': 'Mariusz',
        'nazwisko': 'Czerkies',
        'email': 'mczerkies@wsbcode.pl'
    },
    {
        'imie': 'Tomasz',
        'nazwisko': 'Dluski',
        'email': 'tomasz.dluski@studentpartner.com'
    }
]
print(listaSlownikow[1]['email'])
