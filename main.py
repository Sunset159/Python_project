import random

def generate_number(length):
    digits = list('0123456789')
    random.shuffle(digits)
    if digits[0] == '0':
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(digits[:length])

def bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls  
    return bulls, cows

def start_game():
    total_games = 0
    attempts_list = []
    f = True

    while f == True:
        length = input_number()
        secret = generate_number(length)
        attempts = 0

        print(f"Сгенерировано число из {length} цифр. Начинаем игру!")
        while True:
                guess = input("Введите вашу попытку: ").strip()
                if len(guess) != length or not guess.isdigit():
                    print(f"Попытка должна быть числом из {length} цифр. Попробуйте еще раз.")
                    continue

                attempts += 1
                bulls, cows = bulls_and_cows(secret, guess)
                print(f"Быки: {bulls}, Коровы: {cows}")

                if bulls == length:
                    print(f"Поздравляем! Вы угадали число {secret} за {attempts} попыток.")
                    attempts_list.append(attempts)
                    total_games += 1
                    break
        answer = input("\nПродолжить игру?(Да/Нет): ").strip().lower()
        if(answer == "да"):
            f = True
        else:
            best = min(attempts_list)
            worst = max(attempts_list)
            average = sum(attempts_list) / len(attempts_list)
            print("\nСтатистика игр\n"
                  f"Сыграно: {total_games}\n"
                  f"Лучший результат: {best}\n"
                  f"Средний результат: {average:.2f}\n"
                  f"Худший результат: {worst}")
            f = False

def input_number():
    while True:
        length = input("Введите длину числа (3-5): ").strip()
        if length in {'3', '4', '5'}:
            length = int(length)
            return length
        else:
            print("Ошибка: введите число от 3 до 5.")

if __name__ == '__main__':
    start_game()
