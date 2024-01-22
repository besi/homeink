from inkplate6COLOR import Inkplate
import time

from machine import RTC

display = Inkplate()

# Main function
if __name__ == "__main__":
    rtc = RTC()
    now = (2024, 1, 22, 1, 23, 56, 0, 0)
    rtc.init(now)
    #rtc.datetime(
    #    (2023, 1, 6,
    #     6,   # weekday, domingo es 0 o 7
    #     18, 14, 0, 0)) # set a specific date and time

    print (rtc)
    print (rtc.datetime())
    print (time.localtime(time.time()))


    display.begin()
    display.clearDisplay()
    display.display()

    _,_,_,hour,minute,second,_,_ = time.localtime(time.time())

    hora = str(hour)
    minuto = str(minute)

    display.setTextSize(20)
    display.printText(50,100, hora + ":" + minuto)
    display.display()
    