import random


def create_pole(pole, size_y, size_x, empty_cell):
    for i in range(size_y):
        pole.append([])
        for j in range(size_x):
            pole[i].append(empty_cell)


def show_pole(pole):
    for row in pole:
        for cell in row:
            print(cell, end=" ")
        print()


def user(pole, size_y, size_x, empty_cell, user_cell):
    while True:
        pos_y = input("Введите номер строки (0-2): ")
        pos_x = input("Введите номер столбца (0-2): ")

        if pos_y.isdigit() and pos_x.isdigit():
            pos_y = int(pos_y)
            pos_x = int(pos_x)

            if pos_y < size_y:
                if pos_x < size_x:
                    if pole[pos_y][pos_x] == empty_cell:
                        pole[pos_y][pos_x] = user_cell
                        break
                    else:
                        print("Эта клетка уже занята")
                else:
                    print("Столбец должен быть от 0 до", size_x - 1)
            else:
                print("Строка должна быть от 0 до", size_y - 1)
        else:
            print("Нужно вводить только числа")


def bot(pole, size_y, size_x, empty_cell, bot_cell):
    while True:
        pos_y = random.randint(0, size_y)
        pos_x = random.randint(0, size_x)

        if pole[pos_y][pos_x] == empty_cell:
            pole[pos_y][pos_x] = bot_cell
            break


def win():
    return


size_y = 3
size_x = 3

pole = []

empty_cell = '[_]'
bot_cell = '[0]'
user_cell = '[X]'

create_pole(pole, size_y, size_x, empty_cell)

while True:
    show_pole(pole)
    # if win() == :
    #     break
    user(pole, size_y, size_x, empty_cell, user_cell)
    bot(pole, size_y - 1, size_x - 1, empty_cell, bot_cell)