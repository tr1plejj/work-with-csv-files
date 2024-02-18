from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def move_data():
    var = int(input('Из какого файла перенести данные?\n'
                    '1 - из первого во второй\n'
                    '2 - из второго в первый\n'
                    'Ваш выбор: '))
    
    while var < 1 or var > 2:
        var = int(input('Ошибка. Введите номер действия: '))
    
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            all_data = []
            new = []
            for i in data:
                if i != '\n':
                    new.append(i)
                else:
                    all_data.append(new)
                    new = []
            for i in range(len(all_data)):
                print(f"{i} - {' '.join(all_data[i])}")
            a = int(input('Какую запись вы хотите перенести? (Отсчет идет с 0): '))
            
            while a < 0 or a >= len(all_data):
                a = int(input('Ошибка. Такой записи нет. Введите еще раз: '))

            data_to_move = all_data[a]
            for i in range(len(data_to_move)):
                data_to_move[i] = data_to_move[i].strip('\n')
            data_to_move = f'{data_to_move[0]};{data_to_move[1]};{data_to_move[2]};{data_to_move[3]}\n\n'
            with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
                file.write(data_to_move)
            # без понятия как сделать удаление в файле по нужным данным
                    
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data = ''.join(data).split('\n')
            all_data = []
            for i in data:
                if i != '':
                    new_wr = ''.join(i).split(';')
                    all_data.append(new_wr)
            for i in range(len(all_data)):
                print(f"{i} - {' '.join(all_data[i])}")
            a = int(input('Какую запись вы хотите перенести? (Отсчет идет с 0): '))
            
            while a < 0 or a >= len(all_data):
                a = int(input('Ошибка. Такой записи нет. Введите еще раз: '))
            
            data_to_move = all_data[a]
            data_to_move = f'{data_to_move[0]}\n{data_to_move[1]}\n{data_to_move[2]}\n{data_to_move[3]}\n\n'
            with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
                file.write(data_to_move)
            # без понятия как сделать удаление в файле по нужным данным
