class Pump:
    TYPE = None

    def __init__(self, pump_number):
        self.pump_number = pump_number
        self.assigned_car = None
        self.fuel_count = 0

    def __str__(self):
        return 'Pump ' + str(self.pump_number)

    def is_empty(self):
        if self.assigned_car is None:
            return True
        else:
            return False

    def get_fuel_count(self):
        return self.fuel_count

    def assign(self, car):
        print('{} assigned to {}'.format(car, self))
        self.assigned_car = car

    def fuel(self):
        self.assigned_car.fill_tank(1)
        self.fuel_count += 1
        if self.assigned_car.is_tank_full():
            print(str(self) + ' finished ' + str(self.assigned_car))
            self.assigned_car = None


class GasolinePump(Pump):
    TYPE = 'GASOLINE'

    def __str__(self):
        return 'Gasoline Pump ' + str(self.pump_number)


class DieselPump(Pump):
    TYPE = 'DIESEL'

    def __str__(self):
        return 'Diesel Pump ' + str(self.pump_number)
