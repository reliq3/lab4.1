import random
def generate_schedule(num_exams, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    hours = list(range(9, 15))
    minutes = ["00", 30]
    for i in range(num_exams):
        subject = random.choice(subjects)
        day = random.choice(days_of_week)
        time = f"{random.choice(hours)}:{random.choice(minutes)}"
        ticket = random.randint(1, 20)
        print(f"Экзамен по дисциплине «{subject}» состоится в {day} в {time}. Ваш счастливый билет {ticket}.")
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименование дисциплин через запятую и пробел: ").split(", ")
generate_schedule(num_exams, subjects)