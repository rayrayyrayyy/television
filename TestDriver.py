# create test driver program
# import class
from Television import TV
# define function for tv 1
def television_1():
    channel = int(input("TV 1's channel is: "))
    tv_1 = TV()
    tv_1.set_channel(channel)
    tv_1.set_volume(15)
    tv_1.open_tv()
    
# define function for tv 2
def television_2():
    channel = int(input("TV 2's channel is: "))
    tv_2 = TV()
    tv_2.set_channel(channel)
    tv_2.set_volume(25)
    tv_2.open_tv()

# import module
from tkinter import *
main = Tk()
main.title("Test Driver")
main.minsize(200, 200)
main.maxsize(400, 400)
main.geometry("300x200+800+350")
main.config(bg = "brown")

mainloop() # end program