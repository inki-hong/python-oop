from gas_station import GasStation
from pump import Pump
from car import GasolineCar, DieselCar

station = GasStation()
print('# of pumps:', station.get_number_of_pumps())
assert station.get_number_of_pumps() == 3
pump_1 = station.get_pump(0)
pump_2 = station.get_pump(1)
pump_3 = station.get_pump(2)
assert isinstance(pump_1, Pump)
assert isinstance(pump_2, Pump)
assert isinstance(pump_3, Pump)
pumps = station.get_pumps()
assert isinstance(pumps, list)
for p in pumps:
    print(p, p.is_empty())

##############################

car_list = []
for i in range(15):
    import random
    r = random.random()
    if r > 0.5:
        car = GasolineCar()
    else:
        car = DieselCar()
    car_list.append(car)
for car in car_list:
    print(car)
print('Simulation Start', '-' * 40)

##############################

while len(car_list) > 0 or station.get_number_of_served() < 15:
    if len(car_list) > 0:
        c = car_list[0]
        del car_list[0]
        station.arrive(c)
    station.serve()

print('# of served cars', station.get_number_of_served())
print('$ earned', station.get_revenue())
print('Simulation End', '-' * 40)
