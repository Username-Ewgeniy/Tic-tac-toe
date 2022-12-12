field = [['-'] * 3 for _ in range(3)]

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))


def users_input(f, user):
    while True:
        place = input(f"Ходит {user} .Введите координаты:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        
        #is digit str
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue

        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue

        if f[x][y]!='-':
            print('Клетка занята')
            continue

        break
    
    return x,y


def win_1(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[0][2], f[1][1], f[2][0], user):
            return True

def start(field):

    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = users_input(field, user)
            field[x][y] = user

        elif count == 9:
            print('Ничья')
            break
        
        if win_1(field, user) == True:
            print(f"Выиграл {user}")
            show_field(field)
            break
        count += 1


start(field)
