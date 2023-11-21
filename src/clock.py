import time
from hal import hal_lcd as LCD


def timelcd(lcd):
    local_time = time.localtime() # get struct_time
    time_string1 = time.strftime("%H:%M:%S", local_time)
    time_string2 = time.strftime("%D:%M:%Y", local_time)
    lcd.lcd_display_string(time_string1, 1)
    lcd.lcd_display_string(time_string2, 2)
    time.sleep(0.5)
    lcd.lcd_display_string(" ",1,2)
    lcd.lcd_display_string(" ",1,5)
    lcd.lcd_display_string(" ",2,8)
    lcd.lcd_display_string(" ",2,11)
    time.sleep(0.5)
    timelcd(lcd)

def main():
    lcd = LCD.lcd()
    timelcd(lcd)


if __name__ == "__main__":
    main()
