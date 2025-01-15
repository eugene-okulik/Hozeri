import datetime

input_date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(input_date, '%b %d, %Y - %H:%M:%S')
human_month = python_date.strftime('%B')
human_date = python_date.strftime('%d.%m.%Y, %H:%M')

print(human_month)
print(human_date)