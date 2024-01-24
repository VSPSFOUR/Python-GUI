from  tkinter import * 
window = Tk() 
window.title("Scale GUI")
window.config(bg="white")

def shrink_image(img:PhotoImage, new_width:int, new_height:int) -> PhotoImage:
    width_ratio = img.width() // new_width
    height_ratio = img.height() // new_height

    small_image = img.subsample(width_ratio, height_ratio)
    return small_image 
    
fire_img = shrink_image(PhotoImage(file="fire.png"), 50, 50)


fire_label = Label(master=window, image=fire_img, bg="red")
fire_label.pack()
scale=Scale(master=window,
            from_=100,
            to_= 0,
            length=500, # length of scale
            orient="vertical",# orietation of the scale
            font=("Times New Roman", 12),
            tickinterval=10, # iterval that is shown on side bar 
            showvalue=1, # 0-does not show current value,
            bg="white",
            fg="black",
            troughcolor="lightblue",
            activebackground="grey",
            resolution=5, # the increment the value change in
            width=50
            )
scale.set(50) # sets the defaults start value
scale.pack()
ice_img = shrink_image(PhotoImage(file="ice.png"), 50, 50)
ice_label = Label(window, image=ice_img, bg="blue")
ice_label.pack()
def get_temp():
    print(f"{scale.get()}°C")
get_temp_button = Button(master= window, text="Submit", command=get_temp , width=25)
get_temp_button.pack()
window.mainloop()