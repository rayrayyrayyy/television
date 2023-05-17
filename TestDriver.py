# create test driver program

# import modules and class
from Television import TV
tv_1 = TV()
tv_2 = TV()

from tkinter import * 

root = Tk()
root.minsize(300, 300)

# volume
volume_down = Button(root, text = "-", command = TV.volume_down)
volume_down.pack()

volume = Label(root, text = "Volume")
volume.pack()

volume_up = Button(root, text = "+", command = TV.volume_up)
volume_up.pack()


# call methods
# display output
# end program
mainloop()