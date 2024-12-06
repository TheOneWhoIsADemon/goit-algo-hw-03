import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка вхідних даних через if
    if min < 1 or max >50 or quantity < 1 or quantity > (max - min + 1):
        print("Некоректні параметри. Перевірте діапазон або кількість чисел.")
        return []
    #Генеруємо унікальні випадккові числа
    numbers = random.sample(range(min, max +1), quantity)
    # Створюємо числа за зростанням
    return sorted(numbers)

# Приклад
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)