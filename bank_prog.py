def bank_console():
    import os.path
    all_dep = 0
    file_path = "account.txt"                                  # Создаем переменную для проверки наличия файла с указанием суммы на счете
    check_deposit = os.path.exists(file_path)                  # Создаем переменную для цикла (содержит тру или фалс) для определения наличия файла с указанием суммы на счете
    if check_deposit == True:                                  # Сам цикл - проверяет есть ли файл со счетом
        f = open("account.txt", "r")                           # Если есть то открывает файл счета для чтения
        all_dep = int(f.readline())                            # Присваивает переменной программы значение суммы на счете из файла
        print('Ваш баланс составляет: ', all_dep)
    history = {}
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            deposit = 0
            deposit += int(input('Введите сумму на которую хотите пополнить счет: '))
        elif choice == '2':
            summ_purchase = int(input('Введите сумму покупки:'))
            if summ_purchase <= all_dep:
                purchase = input('Введите название покупки: ')
                all_dep -= summ_purchase
                history[purchase] = f"{summ_purchase}"
            else:
                print('Суммы на вашем счете не достаточно для покупки')
        elif choice == '3':
            n = 1
            for i in history:
                print(n, f': Покупка - "{i}"', f'на сумму {history[i]}')
                n += 1
        elif choice == '4':
            file_account = open('account.txt', 'w')        # открываем файл с количеством денег на счете для перезаписи
            file_account.write(str(all_dep))
            file_account.close()
            file_goods = open('goods.txt', 'a')            # открываем файл с покупками для добавления текущего списка покупок в новую строку
            file_goods.write(str(history) + '\n')
            file_goods.close()
            break
        else:
            print('Неверный пункт меню')
        all_dep += deposit
        deposit = 0
        print('Ваш депозит составляет: ', all_dep)
        print('Выберите пункт меню:')

