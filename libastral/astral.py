import random
import os

# Функция превед
def generate_astral_message():
    messages = ["Превед медвед!", "Кревед!", "Здаров Ромыч!"]
    chosen_message = random.choice(messages)

    # Создание файла и запись выбранного сообщения
    with open("Привет из Астрала.txt", "w", encoding="utf-8") as file:
        file.writelines(chosen_message)

    os.startfile("Привет из Астрала.txt")

# Функция Астрализация
def create_astral_folder():
    # Генерация пути для папки
    base_dir = os.path.expanduser("~")  # Домашний каталог
    random_dir = os.path.join(base_dir, "Астрал_" + str(random.randint(0, 9999)))

    # Создание папки
    os.makedirs(random_dir, exist_ok=True)

    print(f"Папка 'Астрал' была создана по пути: {random_dir}")
    input('Нажмите "Enter" для выхода\n')

# Функция Astral Game
def guess_the_number():
    def convert():
        secret_number = random.randint(1, 10)
        attempts = 0

        print("Попробуйте угадать число от 1 до 10!")

        user_guess = int(input("Введите ваше число: "))
        attempts += 1

        while user_guess != secret_number:

            if user_guess < secret_number:
                print("Число больше, попробуйте еще раз!")
                user_guess = int(input("Введите ваше число: "))
                attempts += 1

            else:
                print("Число меньше, попробуйте еще раз!")
                user_guess = int(input("Введите ваше число: "))
                attempts += 1

        if attempts <= 3:

            print("Вау! Круто!")

        else:

            print("Неплохо, но можно и быстрее.")

    convert()
    while True:
        flag = input('Ещё раз? [1 - да/2 - нет]: ')

        if flag == '1':
            convert()
        else:
            break