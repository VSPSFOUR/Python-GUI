from tkinter import *

window = Tk()
# window.geometry("400x400")
window.config(bg="white")
window.title("Checkboxes GUI")
x = IntVar()


def display_x():
    if x.get() == 1:
        print("checked")
    else:
        print("unchecked")
img = PhotoImage(file="Happy-Emoji-PNG.png", )
smallImage = img.subsample(2,2)
check_button = Checkbutton(
    master=window,
    text="i am a check button",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display_x,
    bg="black",
    fg="green",
    font=("Times New Roman", 32),
    activebackground="green",
    activeforeground="black",
    padx=25, 
    pady = 10,
    image=smallImage,
    compound="right"
)
# onValue - value the x var store if checkbox is clicked
# offValue - value the x var stores if checkbox is not clicked

check_button.pack()
window.mainloop()
