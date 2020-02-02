#! /usr/bin/python
import math

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

CENTERX = 250
CENTERY = 250
LARGEST_RADIUS = distance(CENTERX, CENTERY, 500,500)
f = open("image.ppm", "w+")
f.write("P3\n500 500\n255\n")
image = [[[0 for i in range(3)] for i in range(500)] for i in range(500)]

for y in range(500):
    for x in range(500):
        radius = distance(CENTERX, CENTERY, x, y)
        color = int(255 * radius/ LARGEST_RADIUS)
        image[y][x][0] = color
        image[y][x][1] = color
        image[y][x][2] = color

for y in range(500):
    for x in range(500):
        f.write("" + str(image[y][x][0]) + " " + str(image[y][x][1]) + " " + str(image[y][x][2]) + " ")
f.close()
print("Image File Name: image.ppm")
