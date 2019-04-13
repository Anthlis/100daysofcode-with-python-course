# import actors
from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------------')
    print('     WIZARD GAME')
    print('-------------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    print(creatures)

    hero = Wizard('Gandalf', 75)


    while True:

        cmd = input('Do you [a]ttack, [l]ookaround or [r]unaway? ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'l':
            print('look around')
        elif cmd == 'r':
            print('run away')
        else:
            print('OK... exiting game')
            break


if __name__ == '__main__':
    main()

