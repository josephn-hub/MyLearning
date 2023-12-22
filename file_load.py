

x = 5
y = 6

print(f"\n addtion of 2 numbers to {x + y}")


class Operator:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return str(self.l+self.r)


class Image:
    def __init__(self, x, y):
      self.x = x
      self.y = y

    def size_increase(self):
        self.x = self.x + 200
        self.y = self.y + 300
        return self.x, self.y

    def __repr__(self):
        return f"Changed values of Image size  of x and y are {self.x} and {self.y}"



e1 = Operator(1, 2)

image_size = Image(100, 200)


print(image_size.size_increase())

print(image_size.__repr__())

print(e1)



