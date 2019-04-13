# import actors
import random
import time

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

    # print(creatures)

    hero = Wizard('Gandalf', 75)


    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} '
              f'has appeared from a dark and foggy forest...')

        cmd = input('Do you [a]ttack, [r]unaway or [l]ookaround? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print(f'The Wizard runs and hides taking time to recover....')
                time.sleep(5)
                print(f'The Wizard returns revitalized')

        elif cmd == 'l':
            print(f'The Wizard {hero.name} takes in the surroundings and sees: ')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')

        elif cmd == 'r':
            print('The Wizard has become unsure of its power and flees....')
        else:
            print('OK... exiting game')
            break

        print()


if __name__ == '__main__':
    main()

