class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def square(self):
        print(abs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1)))

    def perimeter(self):
        AB = int(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5)
        BC = int(((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5)
        AC = int(((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2) ** 0.5)
        print(AB + BC + AC)

    def high(self):
        AB = ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
        s = abs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1))
        print(2 * s / AB)


tr = Triangle(-2, 3, 4, 3, 2, 5)
tr.square()
tr.perimeter()
tr.high()