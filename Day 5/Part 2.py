
class point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return str("('") + str(self.x) + str("', '") + str(self.y) + str("')")

def range_between(a, b):
    lower = min(a, b)
    higher = max(a, b)
    
    if a < b:
        return range(lower, higher + 1)
    else:
        return reversed(range(lower, higher + 1))

class vent:
    def __init__(self, a, b):
        self.a = point(a[0], a[1])
        self.b = point(b[0], b[1])
        self.points = self.points_on_line()

    def points_on_line(self):
        x_points = list(range_between(self.a.x, self.b.x))
        y_points = list(range_between(self.a.y, self.b.y))

        if self.a.y == self.b.y: # horizontal
            y_points = [ y_points[0] ] * len(x_points)

        if self.a.x == self.b.x: # vertical
            x_points = [ x_points[0] ] * len(y_points)

        if len(x_points) != len(y_points):
            return set()

        points = set()

        for point in zip(x_points, y_points):
            points.add(point)

        return points

    def __repr__(self):
        return str("{") + str(self.a) + str(", ") + str(self.b) + str("}")

    def intersection(self, other):       
        return self.points.intersection(other.points)

vents = []

with open("Input.txt") as file:
    for line in file:
        words = line.split()
        vents.append(vent(words[0].split(','), words[2].split(',')))

intersections = set()

for vent_1 in vents:
    for vent_2 in vents:
        if vent_1 != vent_2:
            intersections = intersections.union(vent_1.intersection(vent_2))

print(len(intersections))