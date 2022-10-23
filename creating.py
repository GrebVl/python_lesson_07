def new_fail():
    fail_name = str(input('Введите имя фаила: '))
    file_creating = open(f'{fail_name}', 'w', encoding='utf-8')
    print('Создание нового фаила \n'
          '1. Формат 1. \n ФИ Телефон\n'
          '2. Формат 2. \n ФИ \n Телефон\n'
          '3. Выход')
    exit_ = False
    while exit_ == False:
        action_creating = str(input('Выберите действи, через ввод номера: '))
        str_ = ';'
        if action_creating == '1':
            str_fi = str(input('Введите данные: '))
            list_1 = [str_fi, str_, '\n']
            file_creating.writelines(list_1)
        elif action_creating == '2':
            str_f = str(input('Введите фамилию: '))
            str_i = str(input('Введите имя: '))
            str_n = str(input('Введите номер: '))
            str_k = str(input('Введите коментарий: '))
            list_2 = [str_f + '\n', str_i + '\n', str_n + '\n', str_k, str_ + '\n\n']
            file_creating.writelines(list_2)
        elif action_creating == '3':
            exit_ = True
        else:
            print('Введено неверное значение, повторите ввод \n')
    file_creating.close()