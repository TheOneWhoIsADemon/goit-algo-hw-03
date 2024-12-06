from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядокк дати у об'єт
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Поточна дата - можна також використати datetime.now().date()
        today = datetime.today().date()
        # Різниця у днях
        delta = today - input_date
        # Повертаємо кількість днів як ціле число
        return delta.days

    except ValueError:
        # Якщо помила в форматі дати
        print("Неправильний формати дати. Використолвуйте 'PPPP-MM-ДД'")

        return None

# Приклад
days = get_days_from_today("2020-12-06")
if days is not None:
    print(f"Кількість днів: {days}")


