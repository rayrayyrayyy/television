# create test driver program

# import modules and class
from Television import TV
from tkinter import * 

root = Tk()
root.minsize(300, 300)

channel = Button(root, text = "+", command = TV.tv_channel)
channel.pack()

# volume
volume = Label(root, text = "Volume")
volume.pack()

volume_up = Button(root, text = "+", command = TV.volume_up)
volume_up.pack()


# call methods
# display output
# end program
mainloop()