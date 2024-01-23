from tkinter import *

window = Tk()
window.geometry("400x400")
window.config(bg="white")
window.title("Checkboxes GUI")
x = IntVar()

check_button = Checkbutton(master=window, text="i am a check button",
                           variable=x)
check_button.pack()
window.mainloop()
