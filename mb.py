class Control:
    def __init__(self):
        self.x = 4
        self.y = 2
        self.R = self.r2()

    def r2(self):
        return self.x**2 + self.y**2



ctr1 = Control()
#ctr1.x = 10

print(ctr1.x, ctr1.y, ctr1.R)

ctr2 = Control()
print(ctr2.x, ctr2.y, ctr2.r2())


