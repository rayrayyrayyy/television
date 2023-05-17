# Ray Allessandra Pacis | BSCPE 1-5

# create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV
# create class named TV
class TV:

    def __init__(self, channel, volume, power = "OFF"): 
        # create instance variables
        self.channel = channel
        self.volume = volume
        self.power = power

    # define functions for tv
    # Tv channel
    def tv_channel(self):
        self.channel("Enter a channel: ")
        print("Channel was added.")

    # Tv volume
    def volume_up(self):
        '''output message to terminal'''
        print("volume increase")
        

    # Tv power ON/OFf
    def open_tv(self):
        if self.power == "ON":
            print("TV is already ON.")
        else:
            self.power = "ON"
            print("TV is opening.")
        
    def close_tv(self):
        if self.power == "OFF":
            print("TV is already OFF.")
        else:
            self.power = "OFF"
            print("TV is closing.")
