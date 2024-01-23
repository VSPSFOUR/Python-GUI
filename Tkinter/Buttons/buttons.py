from tkinter import *


def greet():
    print("Hello World!")


window = Tk()
window.title("Button GUI")

img = PhotoImage(file="Happy-Emoji-PNG.png")

button = Button(master=window,
                text="Click Me", 
                command=greet,
                font=("Times New Roman", 30,"bold"),
                bg="blue",
                fg="white",
                activebackground="black" ,
                activeforeground="green",
                state = ACTIVE,
                image=img, 
                compound="bottom") # activebackground/activeforeground is teh color that is displayed when hover or clicked
# state=DISABLED makes the button unclickable

button.pack()
window.mainloop()
