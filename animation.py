from turtle import

def draw_shape(sides, length):
    begin_fill()
    for _ in range(sides):
        forward(length)
        right(360 / sides)
        # fillcolor("green")
end_fill()

def draw_matrix(matrix):
    color('yellow')
    speed(100)
    startX = -200
    startY = 200
    shapeSide = 50
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 1:
                fillcolor("blue")
            elif cell == 2:
                fillcolor("grey")
            elif cell == 3:
                fillcolor("green")
            else:
                fillcolor("black")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            penup()
            goto(curX, curY)
            pendown()
            draw_shape(4, shapeSide)

def draw_anime(arrayOfMatrix):
    for matrix in arrayOfMatrix:
draw_matrix(matrix)

matrix1 = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

matrix2 = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 0, 0],
        [0, 0, 2, 1, 1, 2, 0, 0],
        [0, 0, 2, 1, 1, 2, 0, 0],
        [0, 0, 2, 2, 2, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

matrix3 = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 2, 2, 2, 2, 3, 0],
        [0, 3, 2, 1, 1, 2, 3, 0],
        [0, 3, 2, 1, 1, 2, 3, 0],
        [0, 3, 2, 2, 2, 2, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

matrix4 = \
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 3, 3, 3, 3, 3, 1],
        [1, 3, 2, 2, 2, 2, 3, 1],
        [1, 3, 2, 1, 1, 2, 3, 1],
        [1, 3, 2, 1, 1, 2, 3, 1],
        [1, 3, 2, 2, 2, 2, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

smileAnime = [matrix1, matrix2, matrix3, matrix4]

setup(width=600, height=600, startx=0, starty=0)

hideturtle()

draw_anime(smileAnime)

exitonclick()