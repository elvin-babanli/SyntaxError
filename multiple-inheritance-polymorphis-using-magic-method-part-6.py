#-------------------------------------Task_1---------------------------------


class Shape:
    def __str__(self):
        return f"{self.__class__.__name__} with area: {self.area()}"
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
   
    def area(self):
        return self.width * self.height
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height) / 2

class Trapezoid(Shape):
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return ((self.a + self.b) / 2) * self.h


rectangle = Rectangle(5,3)
print(rectangle)

circle = Circle(5)
print(circle)

rightTriangle = RightTriangle(5,4)
print(rightTriangle)

trapezoid = Trapezoid(2,3,5)
print(trapezoid)



#-------------------------------------Task_2---------------------------------

class Shape:
    def __init__(self):
        return int(self.area())
    def __str__(self):
        return f"{self.__class__.__name__} with area: {self.area()}"
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
   
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}, area={self.area()}"

        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __str__(self):
        return f"Circle: Radius={self.radius}, area={self.area()}"

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2
    
    def __str__(self):
        return f"RightTriangle: width={self.base}, height={self.height}, area={self.area()}"

class Trapezoid(Shape):
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return ((self.a + self.b) / 2) * self.h
    
    def __str__(self):
        return f"Trapezoid: width_1={self.a}, width_2={self.b}, height={self.h}, area={self.area()}"





rectangle = Rectangle(5,3)
print(rectangle)

circle = Circle(5)
print(circle)

rightTriangle = RightTriangle(5,4)
print(rightTriangle)

trapezoid = Trapezoid(2,3,5)
print(trapezoid)

#-------------------------------------Task_3---------------------------------


class Shape:
    def __init__(self):
        pass
    def __str__(self):
        pass
    

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(self.x, self.y),
        print(self.x + self.side, self.y),
        print(self.x, self.y + self.side),
        print(self.x + self.side, self.y + self.side)

    def save(self):
        with open("save.txt","w") as file:
            file.write(f"Top Left: {self.x}, {self.y}\n")
            file.write(f"Top Right: {self.x + self.side}, {self.y}\n")
            file.write(f"Bottom Left: {self.x}, {self.y + self.side}\n")
            file.write(f"Bottom Right: {self.x + self.side}, {self.y + self.side}\n")

    def load(self):
        with open("save.txt", "r") as file:
            return file.read()
    

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = height

    def show(self):
        print(self.x, self.y),
        print(self.x + self.width, self.y),
        print(self.x, self.y + self.heigh),
        print(self.x + self.width, self.y + self.heigh)

    def save(self):
        with open("save.txt","w") as file:
            file.write(f"Top Left: {self.x}, {self.y}\n")
            file.write(f"Top Right: {self.x + self.width}, {self.y}\n")
            file.write(f"Bottom Left: {self.x}, {self.y + self.heigh}\n")
            file.write(f"Bottom Right: {self.x + self.width}, {self.y + self.heigh}\n")

    def load(self):
        with open("save.txt", "r") as file:
            return file.read()


class Circle(Shape):
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def show(self):
        print(f"Circle: center=({self.cx}, {self.cy}), radius={self.radius}")

    def save(self):
        with open("save.txt","w") as file:
            file.write(f"Circle: center=({self.cx}, {self.cy}), radius={self.radius}")

    def load(self):
        with open("save.txt", "r") as file:
            return file.read()


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = height

    def show(self):
        print(f"Ellipse: top-left=({self.x}, {self.y}), width={self.width}, height={self.heigh}")
        print(f"Center=({self.x + self.width/2}, {self.y + self.heigh/2})")

    def save(self):
        with open("save.txt","w") as file:
            file.write(f"Ellipse: top-left=({self.x}, {self.y}), width={self.width}, height={self.heigh}")
            file.write(f"Center=({self.x + self.width/2}, {self.y + self.heigh/2})")


def save_shapes(filename, shapes):
    with open(filename, "w", encoding="utf-8") as f:
        for s in shapes:
            if isinstance(s, Square):
                f.write(f"Square {s.x} {s.y} {s.side}\n")
            elif isinstance(s, Rectangle):
                f.write(f"Rectangle {s.x} {s.y} {s.width} {s.heigh}\n")
            elif isinstance(s, Circle):
                f.write(f"Circle {s.cx} {s.cy} {s.radius}\n")
            elif isinstance(s, Ellipse):
                f.write(f"Ellipse {s.x} {s.y} {s.width} {s.heigh}\n")


def load_shapes(filename):
    shapes = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            t = parts[0]
            nums = list(map(float, parts[1:]))

            if t == "Square" and len(nums) == 3:
                x, y, side = nums
                shapes.append(Square(x, y, side))

            elif t == "Rectangle" and len(nums) == 4:
                x, y, w, h = nums
                shapes.append(Rectangle(x, y, w, h))

            elif t == "Circle" and len(nums) == 3:
                cx, cy, r = nums
                shapes.append(Circle(cx, cy, r))

            elif t == "Ellipse" and len(nums) == 4:
                x, y, w, h = nums
                shapes.append(Ellipse(x, y, w, h))
    return shapes

shapes_list = [
    Square(2, 3, 5),
    Rectangle(1, 1, 4, 6),
    Circle(5, 5, 3),
    Ellipse(0, 0, 7, 4)
]

save_shapes("shapes.txt", shapes_list)


loaded_list = load_shapes("shapes.txt")

for i in loaded_list:
    i.show()
