#   a115_buggy_image.py
import turtle as trtl

body = trtl.Turtle()
body.pensize(40)
body.circle(20)

legs = 8
y = 90
z = 380 / legs
body.pensize(5)
n = 0
while (n < legs):
  body.goto (1,25)
  body.setheading(z*n)
  body.forward(y)
  n = n + 1
body.hideturtle()


body.goto(1,25)
body.pencolor("blue")
body.circle(8)
body.penup
body.goto(-15,20)
body.pendown
body.circle(8)


wn = trtl.Screen()
wn.mainloop()