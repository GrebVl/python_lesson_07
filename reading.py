import reading_format as r_f
def reading_fail():
    exit_viewing = False
    while exit_viewing == False:
        print('Просмотр записей: \n'
              '1. Телефонной книги; \n'
              '2. Фаила; \n'
              '3. Выход.')
        action_reading = str(input('Выберите действи, через ввод номера: '))
        if action_reading == '1':
            file_reading = open('phonebook_storege', 'r', encoding='utf-8')
            lines_ = file_reading.read().split()
            file_reading.close()
            r_f.reading_format(lines_)
        elif action_reading == '2':
            fail_name = str(input('Введите имя фаила: '))
            file_reading = open(f'{fail_name}', 'r', encoding='utf-8')
            lines_ = file_reading.read().split()
            file_reading.close()
            r_f.reading_format(lines_)
        elif action_reading == '3':
            exit_viewing = True
        else:
            print('Введено неверное значение, повторите ввод \n')