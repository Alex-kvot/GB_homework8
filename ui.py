from logger import input_data, print_data, modify_data_first_variant, modify_data_second_variant, delete_data_first_variant, delete_data_second_variant

def interface():
    print("Добрый день! Это бот помощник! \n"
          "Что Вы хотите сделать? \n"
          "1 - Записать данные \n"
          "2 - Вывести данные \n"
          "3 - Изменить данные в файле 1 \n"
          "4 - Изменить даныне в файле 2 \n"
          "5 - Удалить данные из файла 1 \n"
          "6 - Удалить данные из фалйа 2 \n" )
    
    command = int(input("Ваш выбор: "))
    while command < 1 or command > 6:
        command = int(input("Ошибка! Попробуйте еще раз! Ваш выбор: "))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        modify_data_first_variant()
    elif command == 4:
        modify_data_second_variant()
    elif command == 5:
        delete_data_first_variant()
    elif command == 6:
        delete_data_second_variant()

