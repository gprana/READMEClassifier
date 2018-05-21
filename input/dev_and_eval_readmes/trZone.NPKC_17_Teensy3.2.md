# NPKC_17_Teensy3.2
NPKC 17 key numpad key tester driven by Teensy 3.2

------------------------------------------------------
NPKC_17_V3.ino

This version has two "layers."

How to change layers: Hold top left button (button 0 in the code), then press slash (button 1)

Each layer has a different set of key codes which are sent to the arduino Keybaord library different ways

FYI: This code is using analogWrite for the LEDS instead of digitalWrite to obtain brightness control, utilizing PWM pins

Layer 0 NUMPAD keys:
This is useful for gaming because games can bind separate commands to numpad_1 and regular 1, for example
- ledPins[0] turns on 
- sends numpad codes, using Keyboard.set_key and Keyboard.send_now because Keyboard.press was not working
- keyHolds array remembers what keys have been pressed /released so that every cycle can send the keys to obtain 6-key rollover

Layer 1 REGULAR keys:
This is useful for using a number pad-like device on a laptop where you can't turn numlock on, as
numlock on a laptop messes up the letters or other keys
- ledPins[1] turns on
- sends regular key codes, using Keyboard.press and Keyboard.release for arduino built-in 6-key rollover
 

------------------------------------------------------
