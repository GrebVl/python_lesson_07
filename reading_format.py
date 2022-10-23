import re


def reading_format(str_):
    print('Формат вывода записей \n'
          '1. Формат 1. \n ФИ Телефон\n'
          '2. Формат 2. \n ФИ \n Телефон\n'
          '3. Выход.')
    exit_format = False
    regex = ';'
    pattern = re.compile(regex)
    while exit_format == False:
        action_reading = str(input('Выберите действи, через ввод номера: '))
        if action_reading == '1' and len(str_) >= 1:
            index = 0
            count = 1
            for i in range(len(str_)):
                if pattern.search(str_[i]):
                    for j in range(index, i, 4):
                        print(f'{count}:', *str_[j:i + 1], sep=' ')
                        count += 1
                    index = i + 1
        elif action_reading == '2' and len(str_) >= 1:
            for i in range(len(str_)):
                if pattern.search(str_[i]):
                    print(f'{str_[i]} \n')
                else:
                    print(f'{str_[i]}')
        elif action_reading == '3':
            exit_format = True
        elif len(str_) < 1:
            print('Записей не имеется \n')
        else:
            print('Введено неверное значение, повторите ввод \n')