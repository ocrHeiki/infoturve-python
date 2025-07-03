import turtle

# Loome turtle objekti
t = turtle.Turtle()

# Joonistame ruudu, 4 külge
for i in range(4):
    t.forward(100)  # Liigume 100 ühikut edasi
    t.right(90)     # Pöörame 90 kraadi paremale

# Lõpetame joonistamise
turtle.done()
