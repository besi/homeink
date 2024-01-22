from inkplate6COLOR import Inkplate
import time


display = Inkplate()

# Main function
if __name__ == "__main__":
    display.begin()
    display.clearDisplay()
    display.display()

    _,_,_,h,m,s,_,_ = time.localtime(time.time())

    hour = str(h)
    minute = ("%02d" % m)

    display.setTextSize(15)
    display.printText(50,100, hour + ":" + minute)
    display.display()
    