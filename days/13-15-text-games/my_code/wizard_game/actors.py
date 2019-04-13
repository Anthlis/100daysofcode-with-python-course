import random


class Wizard:

    def __init__(self, name, the_level):
        self.name = name
        self.level  = the_level

    def attack(self, creature):
        print(f'The wizard {self.name} attacks {creature.name}!')

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * self.level

        print(f'You roll {my_roll}')
        print(f'{creature.name} rolls {creature_roll}')

        if my_roll >= creature_roll:
            print(f'The Wizard has handily triumphed over {creature.name}')
            print()
            return True
        else:
            print(f'The Wizard has been DEFEATED')
            print()



class Creature:
    # level
    # name

    # need to generate instance attributes or instance variables

    # add a magic method as

    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f"Creature {self.name} of level {self.level}"

