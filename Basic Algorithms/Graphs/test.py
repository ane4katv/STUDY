def skyline(buildings):

    x_y_side = []
    for x_1, x_2, y in buildings:
        x_y_side.append((x_1, y, 'left'))
        x_y_side.append((x_2, y, 'right'))

    x_y_side = sorted(x_y_side)

    res = []
    active_heights = []
    cur_max = 0

    for x, y, side in x_y_side:

        if side == 'left':

            active_heights.append(y)

            if y == max(active_heights):
                if res:
                    if res[-1][0] == x:
                        res.pop()

                res.append((x,y))


            cur_max = max(active_heights)

        else:
            popped = active_heights.pop(0)
            if popped == cur_max:
                if not active_heights:
                    res.append((x, 0))
                else:
                    res.append((x, max(active_heights)))


    return res

buildings_1 = [(1,3,3), (2,4,4), (5,8,2), (6,7,4), (8,9,4)]
print(skyline(buildings_1))