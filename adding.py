import adding_format as a_f


def adding_fail():
    exit_viewing = False
    while exit_viewing == False:
        print('Добавление записей: \n'
              '1. Телефонной книги; \n'
              '2. Фаила; \n'
              '3. Выход.')
        action_reading = str(input('Выберите действи, через ввод номера: '))
        if action_reading == '1':
            file_reading = open('phonebook_storege', 'a', encoding='utf-8')
            a_f.adding_format(file_reading)
            file_reading.close()
        elif action_reading == '2':
            fail_name = str(input('Введите имя фаила: '))
            file_reading = open(f'{fail_name}', 'a', encoding='utf-8')
            a_f.adding_format(file_reading)
            file_reading.close()
        elif action_reading == '3':
            exit_viewing = True
        else:
            print('Введено неверное значение, повторите ввод \n')
