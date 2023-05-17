# Ray Allessandra Pacis | BSCPE 1-5

# create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV
# create class named TV
class TV:

    def __init__(self): 
        # create instance variables
        self.channel = 0
        self.volume = 0
        self.power = False

    # define functions for tv
    # Tv channel
    def tv_channel(self):
        self.channel += 1
        print("Channel was added.")
        return self.channel

    # Tv volume
    def volume_up(self) -> None:
        '''output message to terminal'''
        print("volume increase")

    def volume_down(self) -> None:
        '''output message to terminal'''
        print("volume decrease")
        

    # Tv power ON/OFf
    def open_tv(self):
        if self.power == True:
            print("TV is already ON.")
        else:
            self.power = True
            print("TV is opening.")
        
    def close_tv(self):
        if self.power == False:
            print("TV is already OFF.")
        else:
            self.power = False
            print("TV is closing.")

