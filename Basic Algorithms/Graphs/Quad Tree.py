class Quad:
    def __init__(self, borders):
        self.points = []
        self.children = []
        self.borders = borders # (top_left, bottom_right)


class Tree:
    def __init__(self, borders):
        self.main_squad = Quad(borders)

    def divide_to_quads(self, borders, children, points):
        while len(points) > 4:

            mid_x = borders[1][0] / 2
            mid_y = borders[0][1] / 2

            children.append([[borders[0][0], borders[0][1]], [mid_x, mid_y]])
            children.append([[mid_x, borders[0][1]], [borders[1][0], mid_y]])
            children.append([[borders[0][0], mid_y], [mid_x, borders[1][1]]])
            children.append([[mid_x, borders[1][0]], [borders[1][0], borders[1][1]]])


            for top_left, bottom_right in children:
                kid = Quad([top_left, bottom_right])
                if points:
                    for x, y in points:
                        if top_left[0] <= x <= bottom_right[0] and top_left[1] <= y <= bottom_right[1]:
                            kid.points.append([x,y])
                    points = []
                    self.divide_to_quads(kid.borders, kid.children, kid.points)


    def insert(self, point): # point = [x,y]

        # check whether the given node is within the boundaries of the current quad.
        # If it is within the boundaries, we select the appropriate child to contain this node based on its location.
        # If not, do not insert
        pass

    def search(self, point):
        # locate a node in the given quad.
        pass



quad_tree = Tree([[0,6],[3,0]])

