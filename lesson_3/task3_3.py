name = input().title()
age = int(input())
city = input().title()
is_human = True
print("Your name", name, "your age", age, "you live in", city)  # е подойдет?
print(f"Name {name} , age {age} , city {city}")
print("Hello {first_name} , you are {your_age} and live in {living_cyti}".format(first_name=name, your_age=age,
                                                                                 living_cyti=city))
text = "Hello %s age=%s city=%s human?=%s" % (name, age, city, is_human)  # почему при 3х не работает
print(text)
