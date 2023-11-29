import pgzrun
import random
WIDTH=500
HEIGHT=600
alien=Actor("alein")
alien.x=250
alien.y=300
score=0
message=""
def draw ():
    screen.fill("pink")
    alien.draw()
    screen.draw.text(str(score),(50,50))
    screen.draw.text(message,(50,75))
def on_mouse_down(pos):
    global score
    global message

    if alien.collidepoint(pos)==True:
        message="good try"
        alien.x=random.randint(50,450)
        alien.y=random.randint(15,550)
        score=score+1
    else: 
        message="you tried"
pgzrun.go()