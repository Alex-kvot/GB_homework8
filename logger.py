from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
   
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'Записать данные в столбец:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'

                    f'Записать данные в строку:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор?'
                    ))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
            
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print("Данные добавлены в {var} файл")
    


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i

        print(''.join(data_list))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in range(len(data)):
            if data[i] != '\n':
                print(data[i])
            else:
                print()
    
##

def modify_data_first_variant():
    with open('data_first_variant.csv', 'r+', encoding='utf-8') as file:
        data = file.readlines()
        file.seek(0)
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i

        print('Доступные записи:')
        for index, item in enumerate(data_list, start=1):
            print(f"{index}. {item}")

        choice = int(input("Введите номер записи, которую хотите изменить: "))
        if 1 <= choice <= len(data_list):
            new_data = input("Введите новые данные: ")
            data_list[choice - 1] = new_data + '\n'
            file.write(''.join(data_list))
            file.truncate()
            print("Данные успешно изменены.")
            
        else:
            print("Неверный выбор записи.")

def delete_data_first_variant():
    with open('data_first_variant.csv', 'r+', encoding='utf-8') as file:
        data = file.readlines()
        file.seek(0)
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i

        print('Доступные записи:')
        for index, item in enumerate(data_list, start=1):
            print(f"{index}. {item}")

        choice = int(input("Введите номер записи, которую хотите удалить: "))
        if 1 <= choice <= len(data_list):
            data_list.pop(choice - 1)
            file.write(''.join(data_list))
            file.truncate()
            print("Данные успешно удалены.")
            
        else:
            print("Неверный выбор записи.")
        


##

def modify_data_second_variant():
    with open('data_second_variant.csv', 'r+', encoding='utf-8') as file:
        data = file.readlines()
        file.seek(0)
        print('Доступные записи:')
        for index, item in enumerate(data, start=1):
            print(f"{index}. {item.strip()}")

        choice = int(input("Введите номер записи, которую хотите изменить: "))
        if 1 <= choice <= len(data):
            new_data = input("Введите новые данные: ")
            data[choice - 1] = new_data + '\n'
            file.write(''.join(data))
            file.truncate()
            print("Данные успешно изменены.")
            
        else:
            print("Неверный выбор записи.")
        

def delete_data_second_variant():
    with open('data_second_variant.csv', 'r+', encoding='utf-8') as file:
        data = file.readlines()
        file.seek(0)
        print('Доступные записи:')
        for index, item in enumerate(data, start=1):
            print(f"{index}. {item.strip()}")

        choice = int(input("Введите номер записи, которую хотите удалить: "))
        if 1 <= choice <= len(data):
            data.pop(choice - 1)
            file.write(''.join(data))
            file.truncate()
            print("Данные успешно удалены.")
            
        else:
            print("Неверный выбор записи.")
        


