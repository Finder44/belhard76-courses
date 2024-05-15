class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f"Car(color={self.color}, count_passenger_seats={self.count_passenger_seats}, "
                f"is_baby_seat={self.is_baby_seat}, is_busy={self.is_busy})")

class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for car in self.cars:
            if not car.is_busy and car.count_passenger_seats >= count_passengers:
                if is_baby and not car.is_baby_seat:
                    continue
                car.is_busy = True
                return car
        return None


car1 = Car(color="Red", count_passenger_seats=4, is_baby_seat=True)
car2 = Car(color="Blue", count_passenger_seats=4, is_baby_seat=False)
car3 = Car(color="Green", count_passenger_seats=6, is_baby_seat=True)

# Создание автопарка
taxi_fleet = Taxi(cars=[car1, car2, car3])

# Примеры вызовов метода find_car
print(taxi_fleet.find_car(count_passengers=4, is_baby=True))  # Car(color=Red, ...)
print(taxi_fleet.find_car(count_passengers=2, is_baby=False))  # Car(color=Blue, ...)
print(taxi_fleet.find_car(count_passengers=5, is_baby=True))  # Car(color=Green, ...)
print(taxi_fleet.find_car(count_passengers=7, is_baby=True))  # None
print(taxi_fleet.find_car(count_passengers=4, is_baby=True))  # None, все автомобили заняты
