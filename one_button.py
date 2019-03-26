from tkinter import *


def button_clicked():
    root.quit()


root = Tk()
root.title('One button app')
root.geometry('500x400+300+200')
button = Button(root, bg="red", text="Click to quit", command=button_clicked, width=25, height=5)
button.pack(side='top')
root.mainloop()
