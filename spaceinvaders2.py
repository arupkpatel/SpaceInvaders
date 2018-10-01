import turtle
import os
import math
import random


def left():
    x = player.xcor()
    if x > -280:
        x -= playerspeed
        player.setx(x)


def right():
    x = player.xcor()
    if x < 280:
        x += playerspeed
        player.setx(x)


def bulletfire():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    return False

def quit():
    # window.clear()
    endgame = 'Game Over!!!!!!!'
    borderpen.color('white')
    # borderpen.speed(0)
    borderpen.penup()
    borderpen.setposition(0, 0)
    borderpen.write(endgame, False, align='center', font=('Arial', 36, 'bold'))
    window.ontimer(window.bye, 1000)


playerspeed = 20
enemyspeed = 2
bulletspeed = 20
bulletstate = 'ready'
score = 0

images = ['background.gif', 'ship36.gif', 'enemy1.gif', 'turtle2.gif']

# Making of the Screen
window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders : The Mystries CG Assignment - Turtle Edition')
window.setup(700, 700)
window.bgpic(images[0])

# Shape Registration
window.register_shape(images[1])
window.register_shape(images[2])
window.register_shape(images[3])


# Making of the Border
borderpen = turtle.Turtle()
borderpen.speed(0)
borderpen.color('white')
borderpen.penup()
borderpen.setposition(-300, -300)
borderpen.pensize(3)
borderpen.pendown()
for x in range(4):
    borderpen.fd(600)
    borderpen.lt(90)
borderpen.hideturtle()


# Making of the Player
player = turtle.Turtle()
player.color('blue')
player.shape(images[1])
player.penup()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)


#Making of the Enemies
enemies = []
for i in range(5):
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape(images[2])
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(random.randint(-250, 250), random.randint(230, 280))
    enemies.append(enemy)



# Making of the Player Bullet
bullet = turtle.Turtle()
bullet.color('green')
bullet.shape(images[3])
bullet.penup()
bullet.speed(0)
bullet.setposition(0, -400)
bullet.setheading(90)
bullet.shapesize(1, 1)
bullet.hideturtle()


# Keeping Scores
scorepen = turtle.Turtle()
scorepen.penup()
scorepen.color('white')
scorepen.speed(0)
scorepen.setposition(-290,280)
scorestring = 'Score: {}'.format(score)
scorepen.write(scorestring, False, align= 'left', font=('Arial', 12, 'bold'))
scorepen.hideturtle()


# Defining the controls
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')
window.onkeypress(bulletfire, 'space')
window.onkey(quit, 'q')
window.listen()


while True:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if x > 280 or x < -280:
            for e in enemies:
                y = e.ycor()
                e.sety(y - 20)
            enemyspeed = -enemyspeed

        # elif x < -280:
        #     enemy.sety(y - 40)
        #     enemyspeed = -enemyspeed

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bullet.setposition(0, -350)
            enemy.setposition(random.randint(-230, 230), random.randint(230, 280))
            score += 10
            scorestring = 'Score: {}'.format(score)
            scorepen.clear()
            scorepen.write(scorestring, False, align= 'left', font=('Arial', 12, 'bold'))

        if isCollision(player, enemy) or enemy.ycor() > 280:
            quit()

    if bulletstate == 'fire':
        bullet.sety(bullet.ycor() + bulletspeed)

    if bullet.ycor() > 290:
        bulletstate = 'ready'
        bullet.hideturtle()
