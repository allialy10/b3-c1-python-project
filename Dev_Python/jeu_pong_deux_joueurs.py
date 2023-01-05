import turtle 
import winsound

#Creation de l'ecran
ecran = turtle.Screen()
ecran.title('Pong Game') #on met Pong Game comme titre 
ecran.bgcolor ('black') #la couleur du background on la met en noir
ecran.setup(width=800, height=600) #800 en longueur, 600 en largeur


#Initialisation du Score
score_a = 0 
score_b = 0

#Pagaie A
pagaie_a = turtle.Turtle()
pagaie_a.speed(0)
pagaie_a.shape('square') #la forme du pagaie
pagaie_a.color('white')
pagaie_a.shapesize(stretch_wid=5, stretch_len=1) #dimension du pagaie
pagaie_a.penup()
pagaie_a.goto(-350, 0) #position du pagaie


#Pagaie B
pagaie_b = turtle.Turtle()
pagaie_b.speed(0)
pagaie_b.shape('square')
pagaie_b.color('white')
pagaie_b.shapesize(stretch_wid=5, stretch_len=1) #dimension du pagaie
pagaie_b.penup()
pagaie_b.goto(350, 0)

#Trait du milieu
pagaie_m = turtle.Turtle()
pagaie_m.shape('square')
pagaie_m.color('gray')
pagaie_m.shapesize(stretch_wid=50, stretch_len=0.5) #dimension du pagaie
pagaie_m.penup()
pagaie_m.goto(0, 0) #position du pagaie


#Balle 
balle = turtle.Turtle()
balle.speed(0)
balle.shape('circle')
balle.color('white')
balle.penup()
balle.goto(0, 0)
balle.dx = 5
balle.dy = -5

#Ecriture du score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Joeur A: 0 Joeur B: 0" ,align="center", font=("Courier", 24, "normal"))

#Fonctions pour déplacer les pagaies 

def pagaie_a_up():
    y = pagaie_a.ycor() #ycor retourne la coordonnée y 
    y += 20
    pagaie_a.sety(y)

def pagaie_a_down():
    y = pagaie_a.ycor()
    y -= 20
    pagaie_a.sety(y)


def pagaie_b_up():
    y = pagaie_b.ycor()
    y += 20
    pagaie_b.sety(y)

def pagaie_b_down():
    y = pagaie_b.ycor()
    y -= 20
    pagaie_b.sety(y)

#reglage clavier pour faire déplacer les pagaies 
ecran.listen()
ecran.onkeypress(pagaie_a_up, 'e') #fleche gauche pour faire monter le pagaie gauche 
ecran.onkeypress(pagaie_a_down, 'd') #fleche droite pour faire descendre le pagaie gauche 
ecran.onkeypress(pagaie_b_up, 'p')  #fleche gauche pour faire monter le pagaie de droite
ecran.onkeypress(pagaie_b_down, 'm')  #fleche gauche pour faire descendre le pagaie de droite

#pongData = open('pong.csv', 'a+')
#print('x,y,dx,dy,pagaieY', file=pongData)

#mettre à jour l'ecran à chaque fois que l'on joue 
while True:
    ecran.update()


    balle.setx(balle.xcor() + balle.dx)
    balle.sety(balle.ycor() + balle.dy)


    #Collisison de la balle à l'ecran
    if balle.ycor() > 290:
        balle.sety(290)
        balle.dy *= -1
        #winsound.PlaySound('bounce1.wav', winsound.SND_ASYNC)

    if balle.ycor() < -290:
        balle.sety(-290)
        balle.dy *= -1
        #winsound.PlaySound('bounce1.wav', winsound.SND_ASYNC)

    #Faire revenir la balle au centre s'il sort de l'ecran
    if balle.xcor() > 390:
        balle.goto(0, 0)
        balle.dy *= -1
        score_a += 1
        pen.clear()
        pen.write("Joeur A: {} Joeur B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if balle.xcor() < -390:
        balle.goto(0, 0)
        balle.dy *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

   
    #print("{},{},{},{}".format(balle.xcor,balle.ycor,balle.speed,pagaie_b.ycor), file=pongData)
    
    #colisison balle et pagaies 
    if (balle.xcor() > 340 and balle.xcor() < 350) and (balle.ycor() < pagaie_b.ycor() + 40 and balle.ycor() > pagaie_b.ycor() - 40):
        balle.setx(340)
        balle.dx *= -1
        
    if (balle.xcor() < -340 and balle.xcor() > -350) and (balle.ycor() < pagaie_a.ycor() + 40 and balle.ycor() > pagaie_a.ycor() - 40):
        balle.setx(-340)
        balle.dx *= -1
