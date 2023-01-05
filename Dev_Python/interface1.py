from tkinter import *

#la fenetre
fenetre = Tk()
fenetre.geometry('600x600') #la taille de la fenetre
fenetre.title('Menu Pong Game') #le titre de la fenetre 
fenetre['bg'] = 'black' #la couleur du background
fenetre.resizable(height=False,width=False) #je fixe la fenêtre

#le premier texte
label = Label(fenetre, text= "PONG GAME ", font=("Matura MT Script Capitals", 30, "bold"), bg='black', fg="white")
label.place(x='175', y='100') # place le label au point avec les coordonnées x et y

#le deuxieme texte
#label1 = Label(fenetre, text= "Pour demarrer cliquez sur le bouton ci-dessous !", font=("Georgia Pro Cond Black", 10), bg='black', fg="white")
#label1.place(x='135', y='200') #place le label au point avec les coordonnées x et y

#l'image
Monimage = PhotoImage(file='image.png')
label2 = Label(fenetre, image=Monimage)
label2.place(x='150', y='185') #place le label au point avec les coordonnées x et y

#fontion executer le code du jeu
def executer_le_code():
    exec(open("interface2.py", "r").read())

#creation du boutons
bouton = Button(fenetre, text="Demarrer !", font=("Andalus", 15), bg='white', fg='black', command=executer_le_code)
bouton.place(x='250', y='450') #place le bouton au point avec les coordonnées x et y

fenetre.mainloop()



