class Rectangle():
    shape_of_side = 'rectangle'
    no_of_sides = 6
    no_of_vertices = 8
    no_of_edges = 12
    has_curved_surface = False

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.update_area_and_volume()

    def change_x(self, new_x):
        self.x = new_x
        self.update_area_and_volume()

    def change_y(self, new_y):
        self.y = new_y
        self.update_area_and_volume()

    def change_z(self, new_z):
        self.z = new_z
        self.update_area_and_volume()

    def change_xyz(self, new_xyz, x_or_y_or_z):
        if x_or_y_or_z == 'Change X':
            self.change_x(new_xyz)
        elif x_or_y_or_z == 'Change Y':
            self.change_y(new_xyz)
        else:
            self.change_z(new_xyz)

    def update_area_and_volume(self):
        self.area = 2 * (self.x * self.y + self.y * self.z + self.z * self.x)
        self.volume = self.x * self.y * self.z
