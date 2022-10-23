
def menu_click():
    print(' Телефонный спровочник \n'
          '1. Просмотр записей \n'
          '2. Добавление записи в фаил \n'
          '3. Создание нового фаила \n'
          '4. Импорт данных\n'
          '5. Экспорт данных \n'
          '6. Выход')
    choice_action = str(input('Выберите действи, через ввод номера: '))
    if choice_action == '1':
        return 1
    elif choice_action == '2':
        return 2
    elif choice_action == '3':
        return 3
    elif choice_action == '4':
        return 4
    elif choice_action == '5':
        return 5
    elif choice_action == '6':
        return 6
    else:
        print('Введено неверное значение, повторите ввод \n')



