import re


def export_fail():
    exit_exp = False
    regex = ';'
    pattern = re.compile(regex)
    while exit_exp == False:
        print('Формат экспорта \n'
              '1. Формат 1. \n ФИ Телефон\n'
              '2. Формат 2. \n ФИ \n Телефон\n'
              '3. Выход.')
        action_exp = str(input('Выберите действи, через ввод номера: '))
        if action_exp == '3':
            exit_exp = True
            break
        fail_name = str(input('Введите имя фаила: '))
        file_reading = open(f'{fail_name}', 'a', encoding='utf-8')
        file_phonebook = open('phonebook_storege', 'r', encoding='utf-8')
        list_f = file_phonebook.read().split()
        file_reading.write('\n')
        if action_exp == '1' and len(list_f) >= 1:
            for i in range(len(list_f) - 1):
                if pattern.search(list_f[i]):
                    file_reading.write(list_f[i] + '\n')
                else:
                    file_reading.write(list_f[i] + ' ')
        elif action_exp == '2' and len(list_f) >= 1:
            for i in range(len(list_f) - 1):
                if pattern.search(list_f[i]):
                    file_reading.write(list_f[i] + '\n\n')
                else:
                    file_reading.write(list_f[i] + '\n')
        file_reading.close()
        file_phonebook.close()