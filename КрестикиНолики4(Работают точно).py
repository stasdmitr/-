import colorama
# Импортирую, чтобы работать с цветным текстом

from colorama import *

init(autoreset=True)

print(Fore.RED + "Добро пожаловать в игру Крестики нолики v 0.1")
name_first = input(Fore.GREEN + 'Введите имя первого игрока: ')
name_second = input(Fore.BLUE + 'Введите имя второго игрока: ')
print(Fore.RED + "Здравствуйте", Fore.GREEN + name_first, Fore.RED + "и", Fore.BLUE + name_second)

board = list(range(1, 10))
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# Этой фунцией я рисую границы
def draw_board():
    print(Fore.CYAN + ' ---------------')
    for i in range(3):
        print(Fore.CYAN + '|', '', board[0 + i * 3], Fore.CYAN + '|', '', board[1 + i * 3], Fore.CYAN + '|', '',
              board[2 + i * 3], '', Fore.CYAN + '|')
        print(Fore.CYAN + ' ---------------')


def take_input(player_token):
    while True:
        value = input('Куда поставить: ' + player_token + '?')
        if not (value in '123456789'):
            print("Такой клетки не существует, повторите ввод")
            continue
        value = int(value)
        if str(board[value - 1]) in "X0":
            print('Эта клетка уже занята')
            continue
        board[value - 1] = player_token
        break


def check_win():
    for each in wins_coord:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('0')
        if counter > 3:
            winner = check_win()
            if winner == 'X':
                draw_board()
                print(Fore.GREEN + name_first, Fore.GREEN + "Побеждает в этом раунде!)")
                break
            elif winner == '0':
                draw_board()
                print(Fore.BLUE + name_second, Fore.BLUE + "Побеждает в этом раунде!)")
                break

        counter += 1
        if counter > 8:
            draw_board()
            print(Fore.RED + 'Ничья!')
            break


main()
