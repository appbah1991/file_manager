from victory import victorine
from bank_prog import bank_console
import os
import shutil
import platform
while True:
    print('1. создать папку')
    print('2. создать файл')
    print('3. удалить(файл / папку)')
    print('4. копировать(файл / папку)')
    print('5. просмотр содержимого рабочей директории')
    print('6. посмотреть только папки')
    print('7. посмотреть только файлы')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в викторину')
    print('11. мой банковский счет')
    print('12. изменение текущей директории')
    print('13. выход')

    menu_choice = input('Выберите пункт меню: ')
    if menu_choice == '1':
        folder = str(input('Введите название папки: '))
        os.mkdir(folder)
    elif menu_choice == '2':
        text_file = open(str(input('Введите название файла:')), "w")
    elif menu_choice == '3':
        print('Что вы хотите удалить?')
        print('1. файл')
        print('2. папку')
        choise_delete = int(input())
        if choise_delete == 1:
            delete_file = str(input('Введите название файла для удаления:'))
            os.rmdir(delete_file)
        elif choise_delete == 2:
            delete_folder = str(input('Введите название папки для удаления:'))
            os.removedirs(delete_folder)
        else:
            print('Попробуйте ещё раз')
    elif menu_choice == '4':
        print('Что вы хотите копировать?')
        print('1. файл')
        print('2. папку')
        choise_copy = int(input())
        if choise_copy == 1:
            file_to_copy = str(input('Введите название файла который хотите скопировать:'))
            file_copy = str(input('Введите как должен называться новый файл:'))
            shutil.copy(file_to_copy, file_copy)
        elif choise_copy == 2:
            folder_to_copy = str(input('Введите название папки который хотите скопировать:'))
            folder_copy = str(input('Введите как должна называться новая папка:'))
            shutil.copytree(folder_to_copy, folder_copy)
        else:
            print('Попробуйте ещё раз')
    elif menu_choice == '5':
        print(os.listdir())
    elif menu_choice == '6':
        for dirpath, dirnames, filenames in os.walk("."):
            for dirname in dirnames:
                print("Папка:", os.path.join(dirpath, dirname))
    elif menu_choice == '7':
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))
    elif menu_choice == '8':
        os_info = platform.uname()
        print(os_info)
    elif menu_choice == '9':
        Print('Создатель программы - Baha')
    elif menu_choice == '10':
        victorine()
    elif menu_choice == '11':
        bank_console()
    elif menu_choice == '12':
        ch_folder = str(input('Введите название дериктории для замены текущей:'))
        os.chdir(ch_folder)
        print("Текущая директория: ", os.getcwd())
    elif menu_choice == '13':
        break
    else:
        print('Неверный пункт меню')

