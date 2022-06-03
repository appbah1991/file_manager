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
    if menu_choice == '1':                                                          # создать папку
        folder = str(input('Введите название папки: '))
        os.mkdir(folder)
    elif menu_choice == '2':                                                        # создать файл
        text_file = open(str(input('Введите название файла:')), "w")
    elif menu_choice == '3':                                                        # удалить(файл / папку
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
    elif menu_choice == '4':                                                        # копировать(файл / папку)
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
    elif menu_choice == '5':                                                         # просмотр содержимого рабочей директории
        print(os.listdir())
        print('1 - Да')
        print('2 - Нет')
        choise_save_dir = int(input('Хотите сохранить содержимое рабочей директории в файл?'))
        if choise_save_dir == 1:
            listdir_var = open('listdir.txt', 'w', encoding="utf-8")
            list_dir = []
            list_files = []
            for dirpath, dirnames, filenames in os.walk("."):
                for dirname in dirnames:
                    list_dir.append(dirname)
                for filename in filenames:
                    list_files.append(filename)
            list_dir = map(lambda x: x + ', ', list_dir)
            list_files = map(lambda x: x + ', ', list_files)
            listdir_var.write('Папки: ')
            listdir_var.writelines(list_dir)
            listdir_var.write('\n')
            listdir_var.write('Файлы: ')
            listdir_var.writelines(list_files)
            listdir_var.close()
        else:
            exit
    elif menu_choice == '6':                                                         # посмотреть только папки
        for dirpath, dirnames, filenames in os.walk("."):
            for dirname in dirnames:
                print("Папка:", os.path.join(dirpath, dirname))
    elif menu_choice == '7':                                                         # посмотреть только файлы
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))
    elif menu_choice == '8':                                                         # просмотр информации об операционной системе
        os_info = platform.uname()
        print(os_info)
    elif menu_choice == '9':                                                         # создатель программы
        Print('Создатель программы - Baha')
    elif menu_choice == '10':                                                        # играть в викторину
        victorine()
    elif menu_choice == '11':                                                        # мой банковский счет
        bank_console()
    elif menu_choice == '12':                                                        # изменение текущей директории
        ch_folder = str(input('Введите название дериктории для замены текущей:'))
        os.chdir(ch_folder)
        print("Текущая директория: ", os.getcwd())
    elif menu_choice == '13':                                                        # выход
        break
    else:
        print('Неверный пункт меню')

