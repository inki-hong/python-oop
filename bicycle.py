class Bicycle():
    no_of_wheels = 2
    can_go_backwards = False

    def __init__(self, bike_owner='Unknown', gears=4):
        self.owner = bike_owner
        self.no_of_gears = gears

    def __str__(self):
        return 'Bicycle with {} gears owned by {}'.format(
            self.no_of_gears, self.owner
        )

    def set_owner(self, bike_owner):
        self.owner = bike_owner  # chris_bike.owner = 'Chris'

    def set_no_of_gears(self, gears):
        self.no_of_gears = gears


chris_bike = Bicycle()
chris_bike.set_owner('Chris')
chris_bike.set_no_of_gears(5)

david_bike = Bicycle()
david_bike.set_owner('David')
david_bike.set_no_of_gears(6)
