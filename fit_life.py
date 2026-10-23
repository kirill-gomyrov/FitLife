# Проект FitLife - MVP версия 1.0

WATER_ML_PER_KG = 30
ML_PER_LITER = 1000


# 1. Знакомство с пользователем
user_name = input("Введите ваше имя: ")

while True:
    try:
        user_age = int(input("Введите ваш возраст: "))

        if user_age <= 0:
            print("Возраст должен быть больше нуля.")
            continue

        break

    except ValueError:
        print("Некорректный ввод. Укажите возраст целым числом.")


# 2. Сбор данных
while True:
    try:
        user_weight = float(
            input("Введите ваш вес (кг): ").replace(",", ".")
        )

        if user_weight <= 0:
            print("Вес должен быть больше нуля.")
            continue

        break

    except ValueError:
        print("Некорректный ввод. Укажите вес числом.")

while True:
    try:
        user_height = float(
            input("Введите ваш рост (м): ").replace(",", ".")
        )

        if user_height <= 0:
            print("Рост должен быть больше нуля.")
            continue

        break

    except ValueError:
        print("Некорректный ввод. Укажите рост числом.")


# 3. Расчёты

# Индекс массы тела
bmi = user_weight / user_height ** 2

# Суточная норма воды в миллилитрах и литрах
water_ml = user_weight * WATER_ML_PER_KG
water_l = water_ml / ML_PER_LITER


# 4. Вывод результатов
print(f"\nПривет, {user_name}!")
print(f"Возраст: {user_age} лет")
print(f"ИМТ: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print("Расчет окончен. Будьте здоровы!")
