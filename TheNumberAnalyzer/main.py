import math

def AnalyzerNumber():
    number = input_numbers_only()
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    
    print(f"Делители числа {number}: ", divisors)

    simple_number(number)
    perfect_number(number, divisors)

def simple_number(number):
    f = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print(f"Число {number} не является простым")
            f = False
            break
    
    if f == True:
        print(f"Число {number} является простым")

def perfect_number(number, divisors):
    elements = divisors[:-1]
    total = sum(elements)
    expression = "+".join(str(x) for x in elements)
    if number == total:
        print(f"Число {number} является совершенным ({expression}={total})")
    else:
        print(f"Число {number} не является совершенным")

def input_numbers_only():
    while True:
        user_input = input("Введите целое число больше 0: ")
        if user_input.isdigit() or user_input > 0:
            return int(user_input)
        else:
            print("Ошибка: вводите только числа!")

if __name__ == '__main__':
    AnalyzerNumber()