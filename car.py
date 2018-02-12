# -*- coding: utf-8 -*-

import random
import string


class Car:
    MAX_TANK = 5

    def __init__(self):
        x = string.ascii_uppercase + string.digits
        n = []
        for _ in range(4):
            letter = random.choice(x)
            n.append(letter)
        self.plate_no = ''.join(n)
        self.tank = random.randrange(self.MAX_TANK)

    def __str__(self):
        return 'Car {} {}/{}'.format(
            self.plate_no, self.tank, self.MAX_TANK
        )

    def get_tank(self):
        return self.tank

    def fill_tank(self, amount):
        a = amount
        b = self.MAX_TANK - self.tank
        actual = min(a, b)
        self.tank += actual
        print('Filled ' + str(actual) + ' ' + str(self))
        return actual

    def is_tank_full(self):
        # if self.tank == self.MAX_TANK:
        #     return True
        # else:
        #     return False
        return self.tank == self.MAX_TANK


class GasolineCar(Car):
    def __str__(self):
        return 'Gasoline {} {}/{}'.format(
            self.plate_no, self.tank, self.MAX_TANK
        )


class DieselCar(Car):
    MAX_TANK = 6

    def __str__(self):
        return 'Diesel {} {}/{}'.format(
            self.plate_no, self.tank, self.MAX_TANK
        )
