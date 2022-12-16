import random


def game():
    a = random.randint(1, 3)
    print('1 - камень, 2 - ножницы, 3 - бумага')

    player = int(input('Введите число: '))

    if a == 1:
        print('Компьютер выбрал камень')
    elif a == 2:
        print('Компьютер выбрал ножницы')
    elif a == 3:
        print('Компьютер выбрал бумагу')

    if a == player:
        print('Ничья')
    elif a == 1 and player == 2:
        print('Вы проиграли')
    elif a == 1 and player == 3:
        print('Вы выиграли')
    elif a == 2 and player == 1:
        print('Вы выиграли')
    elif a == 2 and player == 3:
        print('Вы проиграли')
    elif a == 3 and player == 1:
        print('Вы проиграли')
    elif a == 3 and player == 2:
        print('Вы выиграли')

    over = input('Хотите сыграть еще? (y/n): ')
    if over == 'y':
        game()

def game2():
    a = random.randint(1, 3)
    print('1 - камень, 2 - ножницы, 3 - бумага')

    player = int(input('Введите число: '))

    if a == 1:
        print('Компьютер выбрал камень')
    elif a == 2:
        print('Компьютер выбрал ножницы')
    elif a == 3:
        print('Компьютер выбрал бумагу')

    ans = player - a
    if ans == 0:
        print('Ничья')
    elif ans == 1 or ans == -2:
        print('Вы выиграли')
    else:
        print('Вы проиграли')

    over = input('Хотите сыграть еще? (y/n): ')
    if over == 'y':
        game2()


if __name__ == "__main__":
    game2()
