class Car():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 {self.load}의 짐을 싣고 주행합니다.')

    def loading(self):
        print(f'최대{self.load}의 짐을 운반할 수 있는 트럭')


class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color)
        self.load = load

class Vehicle(Car):
    def __init__(self, speed, color, seat):
        super().__init__(speed, color)
        self.seat = seat

    def drive(self):
        print(f'{self.speed}로 {self.seat}인의 사람이 타고 주행합니다.')

truck1 = Truck(10, 'red', 1000)
truck1.drive()
car1 = Vehicle(20, 'yellow', 10)
car1.drive()
# car1.loading()