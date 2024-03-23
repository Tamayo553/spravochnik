from logger import input_data, print_data, change_data, delete_data


def interface():
    print("Добрый день вы попали на гиг \n 1 - записать данные \n 2 - ввывод данных \n 3 - изменить данные \n 4 - удалить данные")
    command = int (input('Введите команду '))

    while command != 1 and command != 2 and command !=3 and command !=4 :
        print("не верная команда ")
        command = int(input('Введите '))

    if command == 1:
        input_data()
    elif command ==2:
        print_data()
    elif command ==3:
        change_data()
    elif command ==4:
        delete_data
