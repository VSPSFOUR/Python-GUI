from tkinter import *

window = Tk()
window.title("Entry GUI")

entry = Entry(master=window, font=("Times New Roman", 12), fg="white", bg="black")
entry.insert(0,"Enter Text Here")
entry.pack(side="left")


def displayEntry():
    print(entry.get())
    entry.config(state=DISABLED)  # Disables textbox after submit


submit_button = Button(master=window, text="Submit", command=displayEntry)
submit_button.pack(side="right")


def delete_all():
    entry.delete(0, END)
    # END refers to the end of the str in entry 

delete_button = Button(master=window, text="Clear", command=delete_all)
delete_button.pack(side="right")


def backspace():
    entry.delete(len(entry.get()) - 1, END)


backspace_button = Button(
    master=window, text="<-", font=("Times New Roman", 11), command=backspace
)
backspace_button.pack(side="right")


window.mainloop()
