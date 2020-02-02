#! /usr/bin/python
f = open("image.ppm", "w+")
f.write("P3\n500 500\n255\n")
image = [[[150 for i in range(3)] for i in range(500)] for i in range(500)]
for x in range(500):
    for y in range(500):
        if x == 0:
            image[y][x][0] = 0
            image[y][x][1] = 0
            image[y][x][2] = 0
        else:
            # print(int(255*x / 500))
            image[y][x][0] = int(255*x / 500)
            # image[y][x][0] = 255
            # image[y][x][1] = int(255*x / 500)
            image[y][x][1] = 255
            image[y][x][2] = int(255*y / 500)
            # image[y][x][2] = 255
for y in range(500):
    for x in range(500):
        f.write("" + str(image[y][x][0]) + " " + str(image[y][x][1]) + " " + str(image[y][x][2]) + " ")
f.close()
