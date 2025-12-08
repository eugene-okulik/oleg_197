from datetime import datetime

my_date = "Jan 15, 2023 - 12:05:33"

dt = datetime.strptime(my_date, "%b %d, %Y - %H:%M:%S")

full_month = dt.strftime("%B")
print(full_month)

formatted_date = dt.strftime("%d.%m.%Y, %H:%M")
print(formatted_date)
