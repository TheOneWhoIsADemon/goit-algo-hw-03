import re
# Створюємо функцію
def normalize_phone(phone_number):
    #Видаляємо всі символи, крім цифр та символу "+"
    cleaned_number = re.sub(r'[^\d+]', "", phone_number)
    #Робимо перевірку наявність міжнародного кооду
    if cleaned_number.startswith("+"):
        # Якщо номер починається з "+" то нічого не змінюємо
        return cleaned_number

    elif cleaned_number.startswith("380"):
        #Якщо номер починається з "380" то додаємо "+"
        return "+" + cleaned_number

    else:
        # В інших випадках додаємо код "+38"
        return "+38" + cleaned_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
# Приклад
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)