from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_led as LED
from led_control import *


lcd = LCD.lcd()
lcd.lcd_clear()

led = LED.init()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    if key == 1:
        led_control_init()
        lcd = LCD.lcd()
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blink", 2)
    elif key == 0:
        led_off()
        lcd = LCD.lcd()
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Off", 2)


def main():    
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display something on LCD
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1:Blink", 2)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    


# Main entry point
if __name__ == "__main__":
    main()
