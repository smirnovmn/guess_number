from random import randint

number = randint(1,100)
print('Попробуйте угадать чило от 1 до 100!')

while True:
    inpt = int(input('Введите число в диапазоне от 1 до 100: '))
    if inpt > number:
        print('Ваше число больше того, что загадано')
    elif inpt < number:
        print('Ваше число меньше того, что загадано')
    elif inpt == number:
        print('Отличная интуиция! Вы угадали число :)')
        break


        