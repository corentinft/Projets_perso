from tkinter import *
from tkinter.messagebox import *

main = Tk()
main.geometry("1280x720")
main.title("Pendu")
main.configure(bg="yellow")

#p = PanedWindow(main, height = 720, width = 1280, orient=VERTICAL)
#p.add(Label(p, text='Volet 2', background='white', anchor=CENTER))
#p.add(Label(p, text='Volet 3', background='red', anchor=CENTER))
#p.pack()

canvas1 = Canvas(main, width=1280, height=570, background='#22C8E9"').pack(side=TOP, padx=0)
canvas2 = Canvas(main, width=1280, height=150, background='#FFFFFF"').pack(side=TOP, padx=0)

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(main)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Recommencer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=main.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu2)

main.config(menu=menubar)
main.mainloop()
