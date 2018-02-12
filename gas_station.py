from pump import GasolinePump, DieselPump

class GasStation:
    NUMBER_OF_GASOLINE_PUMPS = 2
    NUMBER_OF_DIESEL_PUMPS = 1
    NUMBER_OF_PUMPS = NUMBER_OF_GASOLINE_PUMPS + NUMBER_OF_DIESEL_PUMPS

    PRICE_PER_UNIT = 2

    def __init__(self):
        self.pumps = []
        for i in range(self.NUMBER_OF_GASOLINE_PUMPS):
            pump = GasolinePump(i + 1)
            self.pumps.append(pump)
        for i in range(self.NUMBER_OF_DIESEL_PUMPS):
            pump = DieselPump(self.NUMBER_OF_GASOLINE_PUMPS + i + 1)
            self.pumps.append(pump)
        self.number_of_served = 0
        self.queue = []

    def get_number_of_pumps(self):
        # return self.NUMBER_OF_PUMPS
        return len(self.pumps)

    def get_pump(self, n):
        return self.pumps[n]

    def get_pumps(self):
        return self.pumps

    def get_number_of_served(self):
        return self.number_of_served

    def arrive(self, car):
        print('{} arrived'.format(car))
        self.queue.append(car)

    def serve(self):
        for pump in self.pumps:
            if pump.is_empty() and len(self.queue) >= 1:
                c = self.queue[0]
                del self.queue[0]
                pump.assign(c)
                break
        for pump in self.pumps:
            if not pump.is_empty():
                print('Serving on', pump)
                pump.fuel()
                if pump.is_empty():
                    self.number_of_served += 1
                break

    def get_revenue(self):
        total_fuel_count = 0
        # a = self.pumps[0].get_fuel_count()
        # b = self.pumps[1].get_fuel_count()
        # c = self.pumps[2].get_fuel_count()
        # total_fuel_count = a + b + c
        for pump in self.pumps:
            total_fuel_count = total_fuel_count + pump.get_fuel_count()
        return total_fuel_count * GasStation.PRICE_PER_UNIT
