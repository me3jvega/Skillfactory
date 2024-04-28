def hello():
    print('''Приветствую в игре  "Крестики-нолики"
Правила просты:
Два игрока ходят по очереди, побеждает тот,
кто первым получит выйгрышную комбинацию.
Ходы объявляются по координатам "X" и "Y"
                                   УДАЧИ!''')


def new_board():
    """Вывод игрового поля"""
    print(f'  0 1 2')
    for i in range(3):  # i изначально равна ' ' проходим i в диапазоне range и ставим i в столбец
        row_info = ' '.join(field[i])  # Тоже самое что и {field[i][0]} {field[i][1]} {field[i][2]}
        print(f'{i} {row_info}')


def step():
    """Спрашивает у пользователя куда он хочет пойти"""
    while True:
        cords = input('Куда желаете пойти? ').split()  # Запрашиваем координаты хода
        if len(cords) != 2:  # Проверяем чтобы было 2 числа
            print('Введите 2 координаты')
            continue
        x, y = cords  # Распаковываем cords и присваиваем их x и y
        if not (x.isdigit()) or not (y.isdigit()):  # Проверяем чтобы были введены числа
            print('Введите число')
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:  # Если x и y в заданном диапазоне
            print('Координаты вне диапазона!')
            continue
        if field[x][y] != ' ':  # И если данное поле пустое то
            print('Клетка занята!')
            continue
        return x, y  # Вернуть x и y


def wins():
    """Проверка выйгрыша"""
    cords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
             ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
             ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
             ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for cord in cords:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print("Выиграл X!!!")
            return True
        if symbols == ['O', 'O', '0']:
            print("Выиграл 0!!!")
            return True
    return False


hello()
field = [[' '] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    new_board()
    if count % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = step()
    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'
    if wins():
        break
    if count == 9:
        print('Ничья!')
        break
