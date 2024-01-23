from tkinter import * 


window = Tk() # instance of window
window.geometry("500x300") # Set size of window.
window.title("Example Window") # Set title
icon  = PhotoImage(file="Color Code Proof.png") # make img a photoimage
window.iconphoto(True, icon) # icon to photoimage 
window.config(background="black") # set background to black

window.mainloop()  # places window on screen & listens for events 
