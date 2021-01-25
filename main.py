import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    startPoint = input("Starting point: ")
    s = tuple(map(int, startPoint.split(',')))
    endPoint = input("Ending point: ")
    e = tuple(map(int, endPoint.split(',')))
    colorImg = cv.imread("maze3.jpg")

    # colorImg  = cv.imread("maze1.png")
    img = cv.imread("maze3.jpg", 0)
    img[s[0]][s[1]] = 1
    img[e[0]][e[1]] = 1
    imgResizeNoColors = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

    edges = cv.Canny(img, 100, 200)
    queue = []
    visited = []

    # backTrack = [[0]*edges.shape[0]] * edges.shape[1]
    backTrack = [[0 for i in range(edges.shape[0])] for j in range(edges.shape[1])]

    queue.append((s[0], s[1]))
    a = (-1, -1)
    while (a != (e[0], e[1])):
        a = queue.pop(0)
        if not (visited.__contains__(a)):
            visited.append(a)
        if not (visited.__contains__((a[0], a[1] - 1)) or edges[a[0]][a[1] - 1] == 255 or queue.__contains__(
                (a[0], a[1] - 1))):  # left or wall
            queue.append((a[0], a[1] - 1))
            backTrack[a[0]][a[1] - 1] = a
        if not (visited.__contains__((a[0], a[1] + 1)) or edges[a[0]][a[1] + 1] == 255 or queue.__contains__(
                (a[0], a[1] + 1))):  # right or wall
            queue.append((a[0], a[1] + 1))
            backTrack[a[0]][a[1] + 1] = a
        if not (visited.__contains__((a[0] + 1, a[1])) or edges[a[0] + 1][a[1]] == 255 or queue.__contains__(
                (a[0] + 1, a[1]))):  # up or wall
            queue.append((a[0] + 1, a[1]))
            backTrack[a[0] + 1][a[1]] = a
        if not (visited.__contains__((a[0] - 1, a[1])) or edges[a[0] - 1][a[1]] == 255 or queue.__contains__(
                (a[0] - 1, a[1]))):  # down or wall
            queue.append((a[0] - 1, a[1]))
            backTrack[a[0] - 1][a[1]] = a
        # if not (visited.__contains__((a[0]+1, a[1] - 1)) or edges[a[0]+1][a[1] - 1] == 255 or queue.__contains__((a[0]+1, a[1] - 1))):  # upper-left or wall
        #     queue.append((a[0]+1, a[1] - 1))
        #     backTrack[a[0]+1][a[1] - 1] = a
        # if not (visited.__contains__((a[0]+1, a[1] + 1)) or edges[a[0]+1][a[1] + 1] == 255 or queue.__contains__((a[0]+1, a[1] + 1))):  # uuper-right or wall
        #     queue.append((a[0]+1, a[1] + 1))
        #     backTrack[a[0]+1][a[1] + 1] = a
        # if not (visited.__contains__((a[0] - 1, a[1]+1)) or edges[a[0] - 1][a[1]+1] == 255 or queue.__contains__((a[0] - 1, a[1]+1))):  # down&right or wall
        #     queue.append((a[0] - 1, a[1]+1))
        #     backTrack[a[0] - 1][a[1]+1] = a
        # if not (visited.__contains__((a[0] - 1, a[1]-1)) or edges[a[0] - 1][a[1]-1] == 255 or queue.__contains__((a[0] - 1, a[1]-1))):  # down&left or wall
        #     queue.append((a[0] - 1, a[1]-1))
        #     backTrack[a[0] - 1][a[1]-1] = a
        #
    path = [(e[0], e[1])]
    b = (-1, -1)
    while (a != (s[0], s[1])):
        a = backTrack[a[0]][a[1]]
        path.append(a)

    for i, j in path:
        colorImg[i][j][0] = 0
        colorImg[i][j][1] = 0
        colorImg[i][j][2] = 255

    print(edges)
    imgResize = cv.resize(colorImg, (500, 500), interpolation=cv.INTER_AREA)

    cv.imshow('image', imgResize)
    cv.waitKey(0)
    cv.destroyAllWindows()