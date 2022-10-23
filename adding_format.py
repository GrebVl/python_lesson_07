def adding_format(str_fail):
    print('Формат записи \n'
          '1. Формат 1. \n ФИ Телефон\n'
          '2. Формат 2. \n ФИ \n Телефон\n'
          '3. Выход')
    exit_format = False
    str_end = ';'
    while exit_format == False:
        action_record = str(input('Выберите действи, через ввод номера: '))
        if action_record == '1':
            str_fi = str(input('Введите данные: '))
            list_1 = [str_fi, str_end + '\n']
            str_fail.writelines(list_1)
        elif action_record == '2':
            str_f = str(input('Введите фамилию: '))
            str_i = str(input('Введите имя: '))
            str_n = str(input('Введите номер: '))
            str_k = str(input('Введите коментарий: '))
            list_2 = [str_f + '\n', str_i + '\n', str_n + '\n', str_k, str_end + '\n']
            str_fail.writelinse(list_2)
        elif action_record == '3':
            exit_format = True
        else:
            print('Введено неверное значение, повторите ввод \n')
    return str_fail