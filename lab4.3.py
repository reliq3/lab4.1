from datetime import datetime, timedelta
def calculate_lucky_dates(start_date, n):
    current_date = datetime.strptime(start_date, "%Y/%m/%d").date()
    lucky_dates = []
    while len(lucky_dates) < 3:
        if current_date.weekday() != 0 and current_date.day % 4 != 0:
            lucky_dates.append(current_date.strftime("%d %B, %A"))
        current_date += timedelta(days=n)
    return lucky_dates
start_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))
lucky_dates = calculate_lucky_dates(start_date, n)
print("Счастливые даты экзамена:")
for date in lucky_dates:
    print(date)
