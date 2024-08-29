class Vehicle:

    def __init__(self, nr_wheels, color, doors_cnt):
        self.nr_wheels = nr_wheels
        self.color = color
        self.doors_cnt = doors_cnt

    def drive(self):
        print("I'm driving, and I'm a vehicle!")

    def describe(self):
        print(f"I'm a {self.color} vehicle, I have {self.nr_wheels} wheels, {self.doors_cnt} doors.(!)")


class Car(Vehicle):
    def __init__(self, color, doors_cnt):
        super().__init__(4, color, doors_cnt)

    def describe(self):
        print("I'm a car, I go vruuum")


v = Vehicle(4,'blue',4)
c = Car('black', 4)
v.describe()
c.describe()