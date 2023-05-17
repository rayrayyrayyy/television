# create test driver program
# import modules and class
from Television import TV
tv_1 = TV()
tv_2 = TV()

from tkinter import * 

root = Tk()
root.minsize(200, 200)
root.title("TV")

# power on/off
power = Label(root, text = "Power")
power.pack()

power_on = Button(root, text = "ON", command = TV.open_tv)
power_on.place(x=40, y=20)

power_off = Button(root, text = "OFF", command = TV.close_tv)
power_off.place(x=120, y=20)

# tv channel

# volume
volume_down = Button(root, text = "-", command = TV.volume_down)
volume_down.place(x=85, y=50)

volume = Label(root, text = "Volume")
volume.place(x=65, y=75)

volume_up = Button(root, text = "+", command = TV.volume_up)
volume_up.place(x=85, y=100)


# call methods
# display output
# end program
mainloop()