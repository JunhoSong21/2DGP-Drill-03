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
    print('BOTTOM')
    for x in range(400, 780, 10):
        draw_boy(x, 90)

def run_right():
    print('RIGHT')
    for y in range(90, 550, 10):
        draw_boy(780, y)

def run_top():
    print('TOP')
    for x in range(780, 20, -10):
        draw_boy(x, 550)

def run_left():
    print('LEFT')
    for y in range(550, 90, -10):
        draw_boy(20, y)

def run_second_bottom():
    print('BOTTOM')
    for x in range(20, 400, 10):
        draw_boy(x, 90)

def run_rectangle():
    print('RECTANGLE')
    run_bottom()
    run_right()
    run_top()
    run_left()
    run_second_bottom()
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 210, 800 // 2, 600 // 2

    for d in range(-90, 270):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy

        draw_boy(x, y)
    pass


while True:
    run_rectangle()
    run_circle()

close_canvas()