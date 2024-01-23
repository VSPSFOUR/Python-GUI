from tkinter import *

window = Tk()
# window.geometry("200x200")
window.config(bg="black")
photo = PhotoImage(file="Color Code Proof.png")

label = Label(
    master=window,
    text="Love is War",
    font=("Times New Roman", 12, "italic"),
    foreground="blue",
    bg="white",
    relief=RAISED,
    bd=10,
    padx=5,  # add paddings between border and text - LHS & RHS 
    pady=5,  # " - Top & Bottom
    image=photo, 
    compound="bottom"
)  # create a label containing text

label.pack()  # add label to window - top center
# label.place(x=0, y=0) # places label in top left




window.mainloop()
