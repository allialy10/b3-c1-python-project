from tkinter import *

#la fenetre
fenetre = Tk()
fenetre.geometry('600x600') #la taille de la fenetre
fenetre.title('Menu Pong Game') #le titre de la fenetre 
fenetre['bg'] = 'black' #la couleur du background
fenetre.resizable(height=False,width=False) #je fixe la fenêtre

#le premier texte
label = Label(fenetre, text= "DEUX JOUEURS", font=("Comic Sans MS", 30, 'bold'), bg='black', fg="white")
label.place(x='150', y='200') # place le label au point avec les coordonnées x et y

label1 = Label(fenetre, text= "JOUEUR A - Touche d : Descendre, Touche e : Monter \n \nJOUEUR B - Touche m : Descendre, Touche p : Monter", font=("Comic Sans MS", 10, 'bold'), bg='black', fg="white")
label1.place(x='135', y='300') #place le label au point avec les coordonnées x et y


def executer_le_code():
    exec(open("jeu_pong_deux_joueurs.py", "r").read())

label2 = Label(fenetre, text= "Pret(e)? CLiquez sur le bouton ci-dessous pour demarrer le jeu !", font=("Comic Sans MS", 10, 'bold'), bg='black', fg="white")
label2.place(x='125', y='400') 

bouton = Button(fenetre, text="Cliquez ici !", bg='white', fg='black', command=executer_le_code)
bouton.place(x='275', y='500') #place le bouton au point avec les coordonnées x et y

fenetre.mainloop()