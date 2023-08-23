import turtle

tatita = turtle.Turtle()
tatita.speed(100000)
for _ in range(20,1000,4):
    tatita.forward(_)
    tatita.right(91)
    tatita.forward(_+1)
    tatita.right(91)
    tatita.forward(_+2)
    tatita.right(91)
    tatita.forward(_+3)
    tatita.right(91)
turtle.done()