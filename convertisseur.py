from tkinter import *
import csv

#je vais mettre des commentaires pour vous montrer que j'ai compris à quoi servent certaines commandes, malgré que le code ne m'appartienne
#pas entièrement, car j'ai un niveau très débutant en python, afin de ne pas être pénalisée

master = Tk()
master.title('Convertisseur de monnaie')
master.geometry('300x300')

#global peut être accessible et modifiée depuis n'importe où dans le code. Lorsqu'on veut accéder ou modifier une variable globale, on
#utilise global pour déclarer qu'on veut accéder à cette variable globale plutôt qu'à une variable locale de même nom.
def fonction():
    global monnaie
    global monnaie2
    global resultat
    global affichage

#label vient de tkinter aussi et va permettre d'afficher une interface avec le bg qu'on lui définit, la taille de la police, etc... 
resultat = Label(master, text = '', font = ('Arial', 20) )
resultat.pack(side = LEFT)

affichage = Entry(master)
affichage.place(x = 10, y = 55)

monnaie = StringVar()
monnaie.set('Euro')
liste_conversions = ['Euro','Dollar',]

monnaie2 = StringVar()
monnaie2.set('Euro')

#l'option menu fait parti de tkinter et va permettre à l'utilisateur d'avoir un sorte de "menu" déroulant en fonction de là où il va cliquer
option1 = OptionMenu(master, monnaie,*liste_conversions) 
option1.place(x = 90, y = 50)

option2 = OptionMenu(master, monnaie2, *liste_conversions)
option2.place(x = 160, y = 50)

# int() renvoie une valeur qui permet de convertir un nombre ou une chaîne de caractères en décimal, tandis que get. est utilisée pour récupérer des informations et 
# les utiliser dans le programme.
def fonction():
    somme = int(affichage.get())
    if monnaie.get() == 'Euro' and monnaie2.get() == 'Euro':
         resultat.config(text = str(somme*1) + 'Euro')

    if monnaie.get() == 'Euro' and monnaie2.get() == 'Dollar':
         resultat.config(text = str(somme*1.22)+ 'Dollar')

    if monnaie.get() == 'Dollar' and monnaie2.get() == 'Dollar':
            resultat.config(text=str(somme * 1) + 'Dollar')

    if monnaie.get() == 'Dollar' and monnaie2.get() == 'Euro':
        resultat.config(text=str(somme * 0.82) + 'Dollar')

#csv va servir de fichier qui va afficher l'historique des commandes sur le convertisseur de monnaie
    with open('conversions.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([monnaie.get(), monnaie2.get(), somme, resultat.cget("text")])
    
button = Button(master, text = 'Convertir', command = fonction)
button.place(x = 200, y = 100)

mainloop()