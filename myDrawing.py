from shapes import Triangle, Rectangle, Oval
rect1 = Rectangle()
rect2 = Rectangle()

rect1.set_width(200)
rect2.set_width(20)
rect1.set_height(100)
rect2.set_height(10)
rect1.set_color("blue")
rect2.set_color("yellow")

rect2.set_x(100)
rect2.set_y(100)

rect1.draw()
rect2.draw()
