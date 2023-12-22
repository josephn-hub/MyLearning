from geometry import rectangle


class GeometryQuestion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def build_rect(self):
        x_point = self.x
        y_point = self.y
        return rectangle(x_point, y_point)


check_rect = GeometryQuestion(5,6)
check_rect.build_rect
print(check_rect)