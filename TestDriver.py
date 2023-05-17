# create test driver program
# import class
from Television import TV
# define function for tv 1
def television_1():
    tv_1 = TV()

# define function for tv 2
def television_2():
    tv_1 = TV()

# import module
from tkinter import *
main = Tk()
main.title("Test Driver")
main.minsize(200, 200)
main.maxsize(400, 400)
main.geometry("300x200+800+350")
main.config(bg = "brown")

mainloop() # end program