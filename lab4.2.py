from datetime import datetime, timedelta
def calculate_exam_date(days_until_exam):
    current_date = datetime.now().date()
    exam_date = current_date + timedelta(days=days_until_exam)
    return exam_date.strftime("%d %B")
days_until_exam = int(input("Введите количество дней до экзамена: "))
exam_date = calculate_exam_date(days_until_exam)
print("Дата экзамена:", exam_date)
