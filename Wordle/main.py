import random

WORDS = ["лотос","столп","комод"]

def check_word(secret, guess):
    feedback = [""] * 5
    secret_letters = list(secret)
    guess_letters = list(guess)

    for i in range(5):
        if guess_letters[i] == secret_letters[i]:
            feedback[i] = f"[{guess_letters[i]}]"
            secret_letters[i] = None
            guess_letters[i] = None
        
        if guess_letters[i] is not None:
            if guess_letters[i] in secret_letters:
                feedback[i] = f"({guess_letters[i]})"
                secret_letters[secret_letters.index(guess_letters[i])] = None
            else:
                feedback[i] = guess_letters[i]   

    return "".join(feedback)

def Wordle_start():
    secret = random.choice([w for w in WORDS])
    attempts = 6
    print("Загадано слово из 5 букв. У Вас 6 попыток.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка {attempt}: ").lower()

        if len(guess) != 5:
            print("Введите слово из 5 букв!")
            continue

        feedback = check_word(secret, guess)
        print(f"Результат: {feedback}")

        if guess == secret:
            print(f"Вы угадали слово '{secret}' за {attempt} попыток")
        else:
            if attempt == 6:
                print(f"Попытки закончились. Загаданное слово: {secret}") 

if __name__ == "__main__":
    Wordle_start()
