"""Игра Крестики - Нолики
Размер поля 3X3"""

ROWS = 3  # Количество строк поля
COLUMNS = 3  # Количество столбцов поля
INDEXES_TO_CHARACTERS = {-1: 'O', 0: '-', 1: 'X'}  # Сопоставление знаков и их индексов
BOOLEANS_TO_INDEXES = {False: -1, True: 1}  # Сопоставление индексов знаков и булевых значений переключателя


def generate_field(rows: int, columns: int) -> list:
    """Функция создания поля"""
    field = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        field.append(row)
    return field


def show_field(field: list):
    """Функция вывода поля на экран"""
    rows = len(field)
    columns = len(field[0])
    print('\n ', end='')
    for i in range(columns):
        print(f' {i}', end='')
    for i in range(rows):
        print(f'\n{i}', end='')
        for j in field[i]:
            print(f' {INDEXES_TO_CHARACTERS[j]}', end='')  # Перевод индексов в знаки для вывода на экран
    print('\n')


def make_move(field: list, character_index: int) -> None | str:
    """Функция совершения хода"""
    print(f'Очередь {INDEXES_TO_CHARACTERS[character_index]}')  # Вывод очереди (X или O)
    row = input('Введите номер ряда (0 - 2): ')
    column = input('Введите номер столбца (0 - 2): ')
    if row.isdigit() and column.isdigit():  # Проверка ввода: введены целочисленные значения
        row = int(row)
        column = int(column)
        if row in range(ROWS) and column in range(COLUMNS):  # Проверка ввода: введены верные координаты
            if field[row][column] == 0:  # Проверка клетки: клетка пуста
                field[row][column] = character_index
            else:
                return 'Неверный ход: Данная клетка уже заполнена\n'
        else:
            return 'Неверный ход: Координаты клетки выходят за границы поля\n'
    else:
        return 'Неверный ход: Введите целочисленные положительные значения для координат\n'


def generate_sequences_to_check() -> list:
    """Функция создания списка последовательностей для проверки"""
    sequences_to_check = []
    for i in range(ROWS):
        row = []
        for j in range(COLUMNS):
            row.append((i, j))
        sequences_to_check.append(row)
    for i in range(COLUMNS):
        column = []
        for j in range(ROWS):
            column.append((j, i))
        sequences_to_check.append(column)
    sequences_to_check.append([(0, 0), (1, 1), (2, 2)])
    sequences_to_check.append([(0, 2), (1, 1), (2, 0)])
    return sequences_to_check


def check_field(field: list) -> str:
    """Функция проверки завершённости игры"""
    for i in SEQUENCES_TO_CHECK:
        sequence_sum = 0
        for j in i:
            sequence_sum += field[j[0]][
                j[1]]  # Операция проверки последовательности: Вычисляется сумма значений для каждой последовательности
        if sequence_sum == 3:
            return 'Победа X!'
        elif sequence_sum == -3:
            return 'Победа O!'
    return 'Ничья'


# Начало программы

game_field = generate_field(ROWS, COLUMNS)  # Создание поля

SEQUENCES_TO_CHECK = generate_sequences_to_check()  # Создание списка последовательностей для проверки

print('Начало игры')  # Начало игры

character_boolean = True  # Объявление булевого значения символа
for move in range(ROWS * COLUMNS):  # Цикл по количеству ходов
    show_field(game_field)  # Вывод поля
    while True:  # Цикл, ожидающий ввода верных координат
        output = make_move(game_field, BOOLEANS_TO_INDEXES[character_boolean])  # Совершение хода
        if output:
            print(output)  # Вывод сообщения о неверном вводе, если оно возникает
        else:
            break  # Продолжение игры при верном вводе координат
    result = check_field(game_field)  # Проверка завершённости игры
    if result != 'Ничья':
        break  # Выход из цикла при обнаружении победы одной из сторон
    character_boolean = not character_boolean  # Изменение булевого значения символа

show_field(game_field)  # Итоговый вывод поля
print(result)  # Вывод результата игры

print('\nКонец игры')  # Конец игры
