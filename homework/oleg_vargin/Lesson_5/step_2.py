text = 'результат операции: 42'
# text = 'результат операции: 514'
# text = 'результат работы программы: 9'

number_str = text[text.index(":") + 2:]
number = int(number_str)
result = number + 10
print(result)
