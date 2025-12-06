i = 11

while True:
    user_input = int(input('Угадай загаданную цифру: '))
    if user_input == i:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
