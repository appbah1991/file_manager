def bank_console():
    all_dep = 0
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
            break
        else:
            print('Неверный пункт меню')
        all_dep += deposit
        deposit = 0
        print('Ваш депозит составляет: ', all_dep)
        print('Выберите пункт меню:')

