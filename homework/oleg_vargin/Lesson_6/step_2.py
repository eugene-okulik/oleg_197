for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FuzzBuzz')
    elif n % 3 == 0:
        print('Fuzz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
