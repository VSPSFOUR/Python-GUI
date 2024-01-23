from tkinter import *

count = 0


def increament():
    global count
    count += 1
    print("Count\t: ", count)


window = Tk()
window.title("Counter")
count_button = Button(
    master=window,
    text="Increment",
    font=("Times New Roman", 11, "bold"),
    fg="black",
    bg="white",
    activebackground="white",
    activeforeground="black",
    command=increament
)
count_button.pack()


window.mainloop()
