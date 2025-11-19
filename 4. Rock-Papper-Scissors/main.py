import random

rules = {
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "спок"],
    "камень": ["ящерица", "ножницы"],
    "ящерица": ["спок", "бумага"],
    "спок": ["ножницы", "камень"],
}

choice = list(rules.keys())

def determine_winner(player, computer, score):
    if player == computer:
        print("Ничья!")
    elif computer in rules[player]:
        print(f"{player.capitalize()} победили {computer} — Вы выиграли!")
        score['Игрок'] += 1
    else:
        print(f"{computer.capitalize()} победили {player} — Вы проиграли!")
        score['Компьютер'] += 1
    return score

def game_start():
    max_wins = 0
    while True:
        try:
            max_wins = int(input("До скольки побед играем?: "))
            if max_wins > 0:
                break
            else:
                print("Введите число больше 0")
        except ValueError:
            print("Введите корректное число")
    
    score = {"Игрок": 0, "Компьютер": 0}

    while score["Игрок"] < max_wins and score["Компьютер"] < max_wins:
        player_choice = input(f"Ваш ход ({', '.join(choice)}): ").strip()
        if player_choice not in choice:
            print("Неверный ход. Попробуйте снова.")
            continue

        computer_choice = random.choice(choice)
        print(f"Компьютер выбрал: {computer_choice}")

        determine_winner(player_choice, computer_choice, score)

        print(f"Счет: Игрок {score['Игрок']} - Компьютер {score['Компьютер']}\n")

    if score["Игрок"] == max_wins:
        print("Поздравляем! Вы выиграли игру!")
    else:
        print("Компьютер выиграл игру! Попробуйте еще раз.")


if __name__ == "__main__":
    game_start()