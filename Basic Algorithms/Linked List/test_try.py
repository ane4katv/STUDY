import heapq


def getSkyline(LRH):

    skyline = []
    i = 0
    n = len(LRH)
    liveHR = []

    while i < n or liveHR:
        if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
            x = LRH[i][0]
            while i < n and LRH[i][0] == x:
                heapq.heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                i += 1
        else:
            x = -liveHR[0][1]
            while liveHR and -liveHR[0][1] <= x:
                heapq.heappop(liveHR)
        height = len(liveHR) and -liveHR[0][0]
        if not skyline or height != skyline[-1][1]:
            skyline += [x, height],
    return skyline


buildings_1 = [(1,3,3), (2,4,4), (5,8,2), (6,7,4), (8,9,4)]
print(getSkyline(buildings_1))