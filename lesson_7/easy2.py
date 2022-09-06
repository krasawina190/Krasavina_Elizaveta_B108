class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

        self.AB = ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
        self.BC = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y2) ** 3) ** 0.5
        self.CD = ((self.x3 - self.x4) ** 2 + (self.y3 - self.y4) ** 2) ** 0.5
        self.AD = ((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2) ** 0.5

    def length(self):
        print("AB = {}, BC = {}, CD = {}, AD = {}".format(self.AB, self.BC, self.CD, self.AD))

    def is_isosceles(self):
        if self.AB==self.CD or self.AD == self.BC:
            print("Трапеция является равнобочной")

    def perimetr(self):
        print("Периметр трапеции =", self.AB+self.BC+self.CD+self.AD)

    def square(self):
        if self.AB==self.CD:
            m = (self.AD+self.BC)//2
            if self.AD<self.BC:
                h = (self.AB**2-((self.BC-self.AD)//2)**2)**0.5
            else:
                h = (self.AB**2-((self.AD-self.BC)//2)**2)**0.5
        elif self.AD==self.BC:
            m = (self.AB+self.CD)/2
            if self.AB<self.CD:
                h = (self.BC ** 2 - ((self.CD - self.AB) // 2) ** 2) ** 0.5
            else:
                h = (self.BC ** 2 - ((self.AB - self.CD) // 2) ** 2) ** 0.5
        print("Площадь трапеции =", round(m*h, 2))

tre = Trapezoid(-1, 0, -1, 3, 4, 6, 4, 0)
tre.is_isosceles()
tre.length()
tre.perimetr()
tre.square()