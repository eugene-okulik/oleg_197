import sys

sys.set_int_max_str_digits(30000)


def fibonacci_generator():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b


num_5 = num_200 = num_1000 = num_100000 = None

fib = fibonacci_generator()
for i in range(100000):
	current = next(fib)
	if i == 4:
		num_5 = current
	elif i == 199:
		num_200 = current
	elif i == 999:
		num_1000 = current
	elif i == 99999:
		num_100000 = current

print(f"5-е число Фибоначчи: {num_5}")
print(f"200-е число Фибоначчи: {num_200}")
print(f"1000-е число Фибоначчи: {num_1000}")
print(f"100000-е число Фибоначчи: {num_100000}")
