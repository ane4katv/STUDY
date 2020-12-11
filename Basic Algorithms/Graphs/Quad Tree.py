class Quad:
    def __init__(self, borders):
        self.points = []
        self.children = []
        self.borders = borders  # [top_left, bottom_right]


class Tree:
    def __init__(self, borders):
        self.main_squad = Quad(borders)

    def __str__(self):
        return str(self.main_squad.borders)

    def add_points(self, points):
        for top_left, bottom_right in points:
            if self.main_squad.borders[0][0] <= top_left <= self.main_squad.borders[1][0] and \
                    self.main_squad.borders[1][1] <= bottom_right <= self.main_squad.borders[0][1]:
                self.main_squad.points.append([top_left, bottom_right])

    def divide_to_quads(self, quad):

        while len(quad.points) > 4:

            kids = []

            mid_x = quad.borders[1][0] / 2
            mid_y = quad.borders[0][1] / 2

            kids.append([[quad.borders[0][0], quad.borders[0][1]], [mid_x, mid_y]])
            kids.append([[mid_x, quad.borders[0][1]], [quad.borders[1][0], mid_y]])
            kids.append([[quad.borders[0][0], mid_y], [mid_x, quad.borders[1][1]]])
            kids.append([[mid_x, quad.borders[1][0]], [quad.borders[1][0], quad.borders[1][1]]])

            print(kids)

            for x, y in quad.points:
                for top_left, bottom_right in kids:
                    if top_left[0] <= x <= bottom_right[0] and top_left[1] <= y <= bottom_right[1]:
                        kid = Quad([top_left, bottom_right])
                        kid.points.append([x, y])
                        quad.children.append(kid)
                        print(quad.children)
                        self.divide_to_quads(kid)

    def insert(self, quad, point):  # point = [x,y]
        pass
        # quad = self.main_squad
        # check whether the given node is within the boundaries of the current quad.
        # if quad.borders[0][0] <= point[0] <= quad.borders[1][0] and quad.borders[1][1] <= point[1] <= quad.borders[0][
        #     1]:
        #         if len(quad.points) == 4:
        #             self.divide_to_quads(quad)
        #             self.insert(quad, point)
        #         else:
        #             quad.points.append(point)
        #     else:
        #         for kid in quad.children:
        #             self.insert(kid, point)

    def search(self, point):
        # locate a node in the given quad.
        pass


tree_borders = [[0, 10], [10, 0]]
quad_tree = Tree(tree_borders)

quad_borders = [[0, 6], [3, 0]]
quad = Quad(quad_borders)

quad_tree.add_points([[1, 1], [1, 2], [2, 1], [3, 0], [3, 1]])

quad_tree.divide_to_quads(quad)
