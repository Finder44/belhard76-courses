name = input()
age = int(input())
city = input()
print("Your name", name, "your age", age, "you live in", city)  # е подойдет?
print(f"Name {name} , age {age} , city {city}")
print("Hello , {first_name} , you are {your_age} , live in {living_cyti}".format(first_name=name, your_age=age,
                                                                                 living_cyti=city))
