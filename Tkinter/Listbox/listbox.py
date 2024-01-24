from tkinter import *


def add_item():
    listbox.insert(listbox.size() + 1, add_item_box.get())
    add_item_box.delete(0, END)
    listbox.config(height=listbox.size())


def submit():
    # get the current selected item
    food = list()
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    for i in food:
        print(i)


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


# def delete():

window = Tk()
window.title("Listbox GUI")
window.config()


listbox = Listbox(
    window,
    bg="#F7FFDE",
    font=("Times New Roman", 12, "italic"),
    width=12,
    selectmode=MULTIPLE,
)
listbox.pack()


listbox.insert(1, "Pizza")
listbox.insert(2, "Paste")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salads")


listbox.config(height=listbox.size())

add_item_box = Entry(master=window, font=("Times New Roman", 12))
add_item_box.pack()


add_item_button = Button(
    master=window, text="Add", font=("Times New Roman", 12), command=add_item
)
add_item_button.pack(side="left")


delete_item_button = Button(
    master=window, text="Delete", font=("Times New Roman", 12), command=delete
)
delete_item_button.pack(side="right")
submit_button = Button(
    master=window,
    text="Submit",
    bg="white",
    font=("Times New Roman", 12),
    command=submit,
)
submit_button.pack()

window.mainloop()
