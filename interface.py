import tkinter as tk 

def sortir_plein_ecran(window):
    window.attributes('-fullscreen', False)
    window.geometry("800x600")

def text(w):
    lab = tk.Label(w , text="choose your difficulty level (easy , normal , hard , demon)"  )
    lab.pack()

def creationFenetre():
    window = tk.Tk()
    window.title("Hangman game !!!")
    return window

def quitButton(window):
    boutonQuitter = tk.Button(window , text ="quit" , command=window.quit)
    boutonQuitter.pack()



def listeDedifficultee(w):
    listbox = tk.Listbox()
    listbox.insert(1 , "easy")
    listbox.insert(2 ,"nomal")
    listbox.insert(3 , "hard")
    listbox.insert(4 , "demon")
    listbox.pack()


w = creationFenetre()
sortir_plein_ecran(w)
text(w)
listeDedifficultee(w)


quitButton(w)
w.mainloop()

