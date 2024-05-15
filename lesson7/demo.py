class Car:
    color: str
    count_passenger_seat: int
    is_baby_seat: bool
    is_busy: bool

    def __init__(self, color, count_passenger_seat, is_baby_seat):
        self.color = color
        self.count_passenger_seat = count_passenger_seat
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f"Info : color = {self.color} , count_passenger_seat = {self.count_passenger_seat} , is_baby_seat = {self.is_baby_seat} , is_busy = {self.is_busy}"



mipo = Car("Purple",3 ,True)
zipo = Car("Red",6,False)
mersedes = Car("White",4,False)
bmw = Car("Black",4,True)
print(zipo)


class Taxi :
    cars : list[Car]
    def __init__(self,cars):
        self.cars=cars

    def find_car(self ,count_passengers, is_baby):
        Car.count_passenger_seat=count_passengers
        Car.is_busy=is_baby

