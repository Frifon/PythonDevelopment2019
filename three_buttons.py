from tkinter import *


def button1_clicked():
    root.quit()


def button2_clicked():
    button2['text'] = 'New text'


def button3_clicked():
    button3.destroy()


root = Tk()
root.title('Three buttons app')
root.geometry('500x400+300+200')
button1 = Button(root, text="Click to quit", command=button1_clicked, width=25, height=5)
button2 = Button(root, text="Click to change text", command=button2_clicked, width=25, height=5)
button3 = Button(root, text="Click to destroy", command=button3_clicked, width=25, height=5)
button1.pack(side='left')
button2.pack(side='top')
button3.pack(side='right')
root.mainloop()
