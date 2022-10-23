import re


def import_fail():
    exit_imp = False
    regex = ';'
    pattern = re.compile(regex)
    while exit_imp == False:
        print('Формат импорта \n'
              '1. Формат 1. \n ФИ Телефон\n'
              '2. Формат 2. \n ФИ \n Телефон\n'
              '3. Выход.')
        action_import = str(input('Выберите действи, через ввод номера: '))
        if action_import == '3':
            exit_imp = True
            break
        fail_name = str(input('Введите имя фаила: '))
        file_reading = open(f'{fail_name}', 'r', encoding='utf-8')
        file_phonebook = open('phonebook_storege', 'a', encoding='utf-8')
        list_f = file_reading.read().split()
        file_phonebook.write('\n')
        if action_import == '1' and len(list_f) >= 1:
            for i in range(len(list_f) - 1):
                if pattern.search(list_f[i]):
                    file_phonebook.write(list_f[i] + '\n')
                else:
                    file_phonebook.write(list_f[i] + ', ')
        elif action_import == '2' and len(list_f) >= 1:
            for i in range(len(list_f) - 1):
                if pattern.search(list_f[i]):
                    file_phonebook.write(list_f[i] + '\n\n')
                else:
                    file_phonebook.write(list_f[i] + '\n')
        file_reading.close()
        file_phonebook.close()