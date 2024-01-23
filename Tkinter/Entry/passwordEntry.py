from tkinter import *

window = Tk()

password_entry = Entry(
    master=window, font=("Times New Roman", 15), fg="black", bg="white", show="*"
)
password_entry.pack(side="left")


def display_password():
    print(password_entry.get())


submit_button = Button(master=window, text="Submit", command=display_password)
submit_button.pack(side="right")
window.mainloop()
