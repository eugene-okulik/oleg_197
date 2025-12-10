PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {
    name: int(price.rstrip('р'))
    for name, price in (line.split() for line in PRICE_LIST.splitlines())
}

print(price_dict)
