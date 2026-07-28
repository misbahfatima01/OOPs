class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        def set_x(self, x):
            self.x = x

        def set_y(self, y):
            self.y = y

        def get_x(self):
            return self.x

        def get_y(self):
            return self.y


class Point3D(Point2D):
    def __init__(self, x, y, z):
       super().__init__(x, y)        # call parent constructor
       self.z = z

    def set_z(self, z):
        self.z = z

    def get_z(self):
        return self.z

class Pen:
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def display(self):
        print("type: " ,self.type)
        print("size: " ,self.size)




