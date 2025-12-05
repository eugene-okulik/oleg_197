# text = 'результат операции: 42'
text = 'результат операции: 514'
# text = 'результат работы программы: 9'

def calc_line(text):
    number = int(text.split(':')[-1])
    print(number + 10)

calc_line(text)
