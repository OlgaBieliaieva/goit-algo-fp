import turtle
import math

def draw_pythagoras_tree(branch_length, depth, angle):
    if depth == 0:
        return
    
    turtle.forward(branch_length)
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, depth - 1, angle)
    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, depth - 1, angle)
    turtle.left(angle)
    turtle.backward(branch_length)


def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()
    
    depth = int(input("Enter recursion depth: "))
    draw_pythagoras_tree(100, depth, 45)
    
    turtle.done()

if __name__ == "__main__":
    main()