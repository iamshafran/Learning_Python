from random import randint


class Die:
    """An attempt to represent a die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, times):
        for x in range(times):
            print(randint(1, self.sides))


SixDie = Die()
SixDie.roll_die(10)

# TenDie = Die(sides=10)
# TenDie.roll_die(10)

# TwentyDie = Die(sides=20)
# TwentyDie.roll_die(10)