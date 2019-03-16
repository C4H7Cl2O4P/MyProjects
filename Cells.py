from turtle import *

def draw_shape(sides, length):
    begin_fill()
    for _ in range(sides):
        forward(length)
        right(360 / sides)
    end_fill()

def draw_matrix(matrix):
    startX = -200
    startY = 200
    shapeSide = 50
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 4:
                fillcolor("blue")
            if cell == 3:
                fillcolor("violet")
            if cell == 2:
                fillcolor("white")
            if cell == 1:
                fillcolor("black")
            if cell == 0:
                fillcolor("gray")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            goto(curX, curY)
            draw_shape(4, shapeSide)

matrix = [
          [2, 2, 2, 2, 2, 2, 2, 2, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 1, 1, 1, 1, 1, 0, 2],
          [2, 0, 1, 3, 3, 3, 1, 0, 2],
          [2, 0, 1, 3, 4, 3, 1, 0, 2],
          [2, 0, 1, 3, 3, 3, 1, 0, 2],
          [2, 0, 1, 1, 1, 1, 1, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 2, 2, 2, 2, 2, 2, 2, 2]
         ]

setup (width=600, height=600, startx=0, starty=0)
color('purple')
hideturtle()

speed(100)
draw_matrix(matrix)

exitonclick()