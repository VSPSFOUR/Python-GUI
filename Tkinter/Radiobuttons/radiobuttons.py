from tkinter import *

window = Tk()
window.title("Radiobuttons GUI")
food_imgs = ["oats.png", "egg.png", "pancake.png"]
food = ["cereal", "eggs", "pancakes"]
x = IntVar()
img_list = []
size = 50

def order():
    print(f"You ordered {food[x.get()]}")
for index in range(len(food)):
    test_image = PhotoImage(file=food_imgs[index])
    width_ratio = test_image.width() // size
    height_ratio = test_image.height() // size

    small_image = test_image.subsample(width_ratio, height_ratio)

    img_list.append(test_image)
    img_list.append(small_image)

    radiobutton = Radiobutton(
        master=window,
        text=food[index],
        variable=x,  # makes radiobutton part of this group
        value=index,  # assign value to each radiobutton
        pady=5,
        padx=2,
        font=("Times New Roman", 12, "italic"),
        image=small_image,
        compound="left",
        indicatoron=0,  # removes circle select & make button selection ?
        width=150,
        selectcolor="green",
        activebackground="lightgreen",
        command=order
    )
    radiobutton.pack(anchor=W)  # Set start of widget from the west wall


def display_x():
    print(x.get())


display_button = Button(master=window, text="Get Value", command=display_x)
display_button.pack()
window.mainloop()
