from swampy.World import world
world = world()
canvas = world.ca(width=1000, height=1200, background='black')
def draw_rectangle(x, y, x1, y1):
    rect = ([x, y], [x1, y1])
    canvas.rectangle(rect, outline='red', width=6, fill='blue')
def draw_rectangle_color(x, y, x2, y2, color):
    rect = ([x, y], [x2, y2])
    canvas.rectangle(rect, outline='white', width=6, fill=color)
def draw_point(x, y, z, color):
    canvas.circle([x, y], z, color)
p1 = 100
p2 = 115
p3 = 120
p4 = 115

def draw_circle(x, y, z, color):
    canvas.circle([x, y], z, color)
draw_circle(90, 100, 115, 'green')
draw_circle(90, 6, 60, 'brown')
draw_circle(90, 90, 45, 'tan')

draw_point(p1, p2, 6, 'blue')
draw_point(p3, p4, 6, 'blue')
draw_rectangle(5, 110, 200, 200)
draw_rectangle_color(35, 250, 160, 200, 'black')

world.mainloop()

