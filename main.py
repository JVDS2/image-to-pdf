from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from tkinter import *

directory = 'images'
extendHeight = 842; 

selected = ''

def createPdf(hType):
    if hType == 'Extender':
        height = 842
    else:
        height = None
    cnv = canvas.Canvas("meupdf.pdf", pagesize=A4)
    for filename in os.listdir(directory):
        cnv.drawImage(f'images/{filename}',0,0, height=height)
        cnv.showPage()
    cnv.save()

def getSelected():
    selected = clicked.get()
    createPdf(selected)

def openFolder():
    path = 'images'
    os.startfile(path)

#colors
bg = "#151555"
bgl = "#5555ff"
fg = "#ffff55"

root = Tk()
root.title('IMAGE TO PDF')
root.geometry('400x300')
root.configure(bg=bg)

options = ['Padrão', 'Extender']

clicked = StringVar(root)
clicked.set(options[0])

mainCanvas = Canvas(root, bg=bg, borderwidth=0, highlightthickness=0)
mainCanvas.place(relx=0.5, rely=0.5, anchor=CENTER)

title = Label(mainCanvas, text='IMAGE TO PDF', bg=bg, fg=fg, font=('Arial',24,'bold'))
title.pack(padx=10, pady=30)

fsCanvas = Canvas(mainCanvas, bg=bg, borderwidth=0, highlightthickness=0)
fsCanvas.pack(padx=10, pady=10)
folderLabel = Label(fsCanvas, text='Coloque as imagens nesta pasta:', bg=bg, fg='white',font=('Arial', 12, 'bold'))
folderLabel.grid(row=1,column=1, padx=10)
folderBtn = Button(fsCanvas, text="ABRIR PASTA", command=openFolder)
folderBtn.grid(row=1,column=2)

ddCanvas = Canvas(mainCanvas, bg=bg, borderwidth=0, highlightthickness=0)
ddCanvas.pack(pady=10)
hMenuLabel = Label(ddCanvas, text='Modo:', bg=bg, fg='white',font=('Arial', 12, 'bold'))
hMenuLabel.grid(row=1,column=1)
hMenu = OptionMenu(ddCanvas, clicked, *options)
hMenu.configure(bg=bgl, highlightthickness=0)
hMenu.grid(row=1,column=2)

createBtn = Button(mainCanvas, text='CRIAR PDF', command=getSelected)
createBtn.pack(pady=20)

root.mainloop()

