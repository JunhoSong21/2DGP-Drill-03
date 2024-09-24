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

def run_top():
    print('TOP')
    for x in range(800, 0, -10):
        draw_boy(x, 550)
    pass

def run_right():
    print('RIGHT')
    pass

def run_bottom():
    print('BOTTOM')
    pass

def run_left():
    print('LEFT')
    pass

def run_rectangle():
    print('RECTANGLE')
    run_bottom()
    run_right()
    run_top()
    run_left()
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
    break

close_canvas()