from random import randint

def select_problem():
    while(True):
        print('Выберите задачу: \n1. Проверка существования треугольника\n'
              '2. Проверка числа на простое/составное\n3. Угадай число')
        try:
            user_choice = user_input_number('соответствующее номеру задания ')
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    triangle()
                    break
                case 2:
                    prime_numbers()
                    break
                case 3:
                    bulls_and_cows()
                    break
                case _:
                    print('Введите корректный номер задачи')
                    continue
        except ValueError:
            print('Введите корректный номер задачи')
            pass


def triangle():
    print('Введите целые числа для проверки существует ли треугольник со сторонами такой длины:')
    message_list = {0:'первое ', 1:'второе ', 2:'третье '}
    tri = []
    for i in range(3):
        while(True):
            try:
                num = user_input_number(message_list[i])
                num = int(num)
                if num > 0:
                    tri.append(num)
                    break
                else:
                    print('Необходимо ввести целое число')
            except ValueError:
                pass
    if tri[0]+tri[1] > tri[2] and tri[1]+tri[2] > tri[0] and tri[0]+tri[2] > tri[1]:
        print('Треугольник существует', end=' ')
        if tri[0] == tri[1] == tri[2]:
            print('и является равносторонним')
        elif tri[0] == tri[1] or tri[1] == tri[2] or tri[0] == tri[2]:
            print('и является равнобедренным')
    else:
        print('Треугольник не существует')

def prime_numbers():
    print('Проверка является ли число простым')
    while(True):
        try:
            num = user_input_number('')
            num = int(num)
            if 0 > num or num > 100000:
                print('Число должно быть больше 0 и меньше 100 тысяч')
                continue
            break
        except ValueError:
            pass
    if num == 2:
        print(f'Число {num} является простым')
    elif num == 1:
        print(f'Число {num} не является ни простым, ни составным')
    elif num != 2 and num % 2 == 0:
        print(f'Число {num} является составным')
    else:
        prime = [2]
        for i in range(3,int(num**(0.5)),2):
            prime.append(i)
        for i in prime:
            if num % i == 0:
                print(f'Число {num} является составным')
                break
            elif i == prime[-1]:
                print(f'Число {num} является простым')

def bulls_and_cows():
    secret_num = randint(0, 1001)
    flag = False
    print('Угадайте загаданное число (от 0 до 1000) за десять попыток')
    for i in range(10):
        while(True):
            try:
                user_num = user_input_number('')
                user_num = int(user_num)
                if 0 <= user_num <= 1000:
                    break
                else:
                    print('Число должно быть от 0 до 1000')
                    continue
            except ValueError:
                pass
        if secret_num == user_num:
            flag = True
            break
        elif secret_num > user_num:
            print('Больше.')
        elif secret_num < user_num:
            print('Меньше.')
    if flag == True:
        print(f'Поздравляю, вы угадали число! Было загадано {secret_num}')
    else:
        print(f'Не повезло. Было загадано {secret_num}')

def user_input_number(message):
    user_number = input(f'Введите {message}число:\n')
    return user_number

select_problem()