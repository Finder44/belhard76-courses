class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f"color {self.color} count_passenger_seats {self.count_passenger_seats} "
                f"is_baby_seat {self.is_baby_seat} is_busy {self.is_busy}")


class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for car in self.cars:
            if not car.is_busy and car.count_passenger_seats >= count_passengers:
                if is_baby:
                    if not car.is_baby_seat:
                        continue
                car.is_busy = True
                return car
        return None#почему вне цикла

car1 = Car("Black" , 4 , False)
car2 = Car("Rad" , 5 , True)
car3 = Car("White" , 4 ,False)
bmw = Car("Blueye" , 6,False)

taxi = Taxi(cars= [car1,car2,car3,bmw])
print(taxi.find_car(2,False))
print(taxi.find_car(4,True))
print(taxi.find_car(5 , False))
print(taxi.find_car(3,False))
print(taxi.find_car(2,False))