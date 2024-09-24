from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def run_bottom():
    for x in range(400, 780, 10):
        draw_boy(x, 90)

def run_right():
    for y in range(90, 550, 10):
        draw_boy(780, y)

def run_top():
    for x in range(780, 20, -10):
        draw_boy(x, 550)

def run_left():
    for y in range(550, 90, -10):
        draw_boy(20, y)

def run_second_bottom():
    for x in range(20, 400, 10):
        draw_boy(x, 90)

def run_rectangle():
    print('RECTANGLE')
    run_bottom()
    run_right()
    run_top()
    run_left()
    run_second_bottom()

def run_circle():
    print('CIRCLE')

    r, cx, cy = 210, 800 // 2, 600 // 2

    for d in range(-90, 270):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy

        draw_boy(x, y)

def run_triangle_bottom():
    for x in range(400, 780, 10):
        draw_boy(x, 90)

def run_triangle_right():
    for x, y in zip(range(780, 400, -10), range(90, 564, 13)):
        draw_boy(x, y)

def run_triangle_left():
    for x, y in zip(range(400, 20, -10), range(564, 90, -13)):
        draw_boy(x, y)

def run_triangle_second_bottom():
    for x in range(20, 400, 10):
        draw_boy(x, 90)

def run_triangle():
    print('TRIANGLE')
    run_triangle_bottom()
    run_triangle_right()
    run_triangle_left()
    run_triangle_second_bottom()

while True:
    run_rectangle()
    run_circle()
    run_triangle()

close_canvas()