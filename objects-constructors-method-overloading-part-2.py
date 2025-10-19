# ----------------------Task_1----------------------
class Car:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.speed = speed
        self.model = model

    def start(self,sound=None):
        if sound is None:
            print(f"Your {self.model} is starting")
        else:
            print(f"Your {self.model} is starting with: {sound}")
    
    def drive(self,speed=None):
        if speed is None:
            print(f"Your {self.brand} {self.model} car is driving ")
        else:
            print(f"Your {self.brand} {self.model} car is driving {speed} km/h")

print("Task 1")
car_1 = Car("BMW","M5",2025)
car_1.start()
car_1.start("vir vir vir")
car_1.drive()
car_1.drive(180)
print()

# ----------------------Task_2----------------------

class Book:
    def __init__(self,name,genre,page):
        self.name = name
        self.genre = genre
        self.page = page

    def start(self,smell=None):
        if smell is None:
            print(f"The book's have {self.page} pages")
        else:
            print(f"The book's smell is {smell} in the {self.page} pages")

    def read(self,color=None):
        if color is None:
            print(f"The book {self.name} with {self.genre} genre of book is reading ")
        else:
            print(f"The book {self.name} with {self.genre} genre book have {self.page} with {color} color")

print("Task 2")
book_1 = Book("Crime and Punishment","Novel",450)
book_1.start()
book_1.start("like that")
book_1.read()
book_1.read("Red")
print()


# ----------------------Task_3----------------------

class Stadium:
    def __init__(self,name):
        self.name = name

    def start(self,color=None):
        if color is None:
            print(f"The stadium name is {self.name}")
        else:
            print(f"The stadium color is {color}")

    def match(self,rival_1 = None, rival_2 = None):
        if rival_1 is None and rival_2 is None:
            print(f"Match playing in the {self.name} stadium")
        else:
            print(f"Match started: {rival_1} vs {rival_2}")

print("Task 3")
match_1 = Stadium("Camp Nou")
match_1.start()
match_1.start("Red and Blue")
match_1.match()
match_1.match("Barcelona","Real Madrid")
