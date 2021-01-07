class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1


def overlapping(p1, p2, q1, q2):
    if p1.x > q2.x or p2.x < q1.x or p1.y > q2.y or p2.y < q1.y:
        return False
    else:
        return True


p1 = Point(1,3)
p2 = Point(4,5)
q1 = Point(3, 4)
q2 = Point(9, 8)

print(overlapping(p1, p2, q1, q2))