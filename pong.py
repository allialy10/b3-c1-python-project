import pygame
from pygame.locals import *
import pygame_menu

pygame.init()

#Dimension de nos fenêtres
screen_width = 600
screen_height = 500

#vitesse de rechargement de la fenêtre
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


#définissions de la police
font = pygame.font.SysFont('Constantia', 30)


#definissions des variables
margin = 50
fps = 60

#definitions des couleurs colours
bg = (50, 25, 50)
white = (255, 255, 255)

#tableau de bord

def draw_board():

	screen.fill(bg)

	pygame.draw.line(screen, white, (0, margin), (screen_width, margin), 2)


#Police du texte
def draw_text(text, font, text_color, x, y):
	img = font.render(text, True, text_color)
	screen.blit(img, (x, y))


# Classe pour la création des raquettes
class paddle():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rect = Rect(x, y, 20, 100)
		self.speed = 5
		self.ai_speed = 5


		
	#fonction pour déplacer les joueurs
	def move(self):
        
		key = pygame.key.get_pressed()
        
		if key[pygame.K_UP] and self.rect.top > margin:
			self.rect.move_ip(0, -1 * self.speed)
		if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
			self.rect.move_ip(0, self.speed)

	def move_first_player(self):

		key = pygame.key.get_pressed()
        
		if key[pygame.K_s] and self.rect.top > margin:
			self.rect.move_ip(0, -1 * self.speed)
	
		if key[pygame.K_w] and self.rect.bottom < screen_height:
			self.rect.move_ip(0, self.speed)


	def ai(self):
		
		if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
			self.rect.move_ip(0, self.ai_speed)
		
		if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
			self.rect.move_ip(0, -1 * self.ai_speed)


	#dessin des raquettes
	def draw(self):
		pygame.draw.rect(screen, white, self.rect)


# classe pour la balle
class ball():
	def __init__(self, x, y):
		self.reset(x, y)


	def move(self):

		#verifier s'il y'a collision en haut
		if self.rect.top < margin:
			self.speed_y *= -1


		#vérifier s'il y'a collision en bas
		if self.rect.bottom > screen_height:
			self.speed_y *= -1


		#verifier s'il y'a collision avec les joueurs
		if self.rect.colliderect(player_paddle) or self.rect.colliderect(player2_paddle) or self.rect.colliderect(cpu_paddle):
			self.speed_x *= -1


		#Vérifier si la balle est sortie du terrain
		if self.rect.left < 0:
			self.winner = 1
		if self.rect.left > screen_width:
			self.winner = -1


		#mise à jour de la balle
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		return self.winner

	

	#dessin de la balle
	def draw(self):
		pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

	#initialisation de la balle	
	def reset(self, x, y):
		self.x = x
		self.y = y
		self.ball_rad = 8
		self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
		self.speed_x = -6
		self.speed_y = 6
		self.winner = 0 


#creation des raquettes
player_paddle = paddle(screen_width - 40, screen_height // 2)
player2_paddle = paddle(20, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)

#creation de balle
pong = ball(screen_width - 60, screen_height // 2 + 50)



#fonction pour lancer le mode un joueur

def one_player(live_ball, winner):

	cpu_score = 0
	player_score = 0
	run = True
	while run:

		fpsClock.tick(fps) #vitesse du jeu


		#affichage des raquettes sur le terrain
		draw_board()
		draw_text('CPU: ' + str(cpu_score), font, white, 20, 15)
		draw_text('Player1: ' + str(player_score), font, white, screen_width - 150, 15)
		
		
		player_paddle.draw()
		cpu_paddle.draw()

		if live_ball == True:
			winner = pong.move()
			
			if winner == 0:
				pong.draw()
				player_paddle.move()
				cpu_paddle.ai()
			else:
				live_ball = False
				if winner == 1:
					player_score += 1
				elif winner == -1:
					cpu_score += 1

		#lorsque la balle est statique on détermine la valeur du winner 
		if live_ball == False:
			if winner == 0:
				draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 -100)
			if winner == 1:
				draw_text('YOU SCORED!', font, white, 220, screen_height // 2 -100)
				draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 -50)
			if winner == -1:
				draw_text('CPU SCORED!', font, white, 220, screen_height // 2 -100)
				draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 -50)


		#Gestion des évenements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
				live_ball = True
				pong.reset(screen_width - 60, screen_height // 2 + 50)
	

		pygame.display.update()





#fonction pour lancer le mode deux joueurs

def two_player(live_ball, winner) :
	player2_score = 0
	player_score = 0
	run = True
	while run:

		fpsClock.tick(fps) # vitesse de jeu


		#affichage des raquettes sur le terrain
		draw_board()
		draw_text('Player1: ' + str(player2_score), font, white, 20, 15)
		draw_text('Player2: ' + str(player_score), font, white, screen_width - 150, 15)
		

		#dessin des joueurs
		player_paddle.draw()
		player2_paddle.draw()


		if live_ball == True:
			winner = pong.move()
			if winner == 0:

				#creation de la ball
				pong.draw()

				#deplacer les raquettes
				player_paddle.move()
				player2_paddle.move2()


			else:
				live_ball = False
				if winner == 1:
					player_score += 1
				elif winner == -1:
					player2_score += 1


		#lorsque la balle est statique on détermine la valeur du winner 
		if live_ball == False:
			if winner == 0:
				draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 -100)
			if winner == 1:
				draw_text('PLAYER 2 SCORED!', font, white, 150, screen_height // 2 -100)
				draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 -50)
			if winner == -1:
				draw_text('PLAYER 1 SCORED!', font, white, 200, screen_height // 2 -100)
				draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 -50)

		#Gestion des évenements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			
			if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
				live_ball = True
				pong.reset(screen_width - 300, screen_height // 2 + 50)
				
			
		pygame.display.flip()




#fonction pour lancer les jeux

def start_the_game_one_player():
	one_player(False, 0)

def start_the_game_two_player():
	two_player(False, 0)



#Creation du menu

menu = pygame_menu.Menu('Welcome', 600, 500, theme=pygame_menu.themes.THEME_BLUE)

#on ajoute des boutons qui lancerons notre jeu
menu.add.button('One Player', start_the_game_one_player)
menu.add.button('Two Player', start_the_game_two_player)
menu.add.button('Quit', pygame_menu.events.EXIT)


#on affiche tout ça sur l'écran
menu.mainloop(screen)


pygame.display.flip()

	
pygame.quit()
