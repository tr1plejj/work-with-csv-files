from logger import input_data, print_data, move_data


def interface():
    print('Добрый день! Это бот помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - записать данные \n'
          '2 - вывести данные \n'
          '3 - перенести данные')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 3:
        command = int(input('Ошибка. Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        move_data()

interface()