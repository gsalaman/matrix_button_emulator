# matrix_button_emulator
Mac-based python window that emulates the 8x8 button grid

## Showstopper!
With my current serial code, I assume that /dev/tty* is available for the device in question, but that leads to a "chicken-and-egg" problem here.  To wit, the Pi code won't run unless the Mac serial (over USB) is present, and the Mac serial code won't run unless the Pi is present.

What this means:  in order to do this solution, I cannot just rely on the serial code wth an already opened tty port...I need to use low level USB drivers to open that tty port prematurely.

One other issue with this solution is there's gonna be a fair amount of custom install on my mac...meaning it'll be harder for others to run their own emulator (although I *could* set up one of the cart laptops with t...)

Potential ways forward
* suck it up and learn the USB stuff
* use an ESP32 as a control device...serial out one end, and either BLE or MQTT out the other end to an app or webpage
* If you are doing that, why not just tweak the get_button code to support either BLE or MQTT?  BLE would be my first choice as I want to learn how to do that on the Pi

Note the middle option has the advantage of looking JUST like our arduino interface, whilst the latter one lets us do remote control of the jumbotron.  Both have merit.

## Moving forward - MQTT
As a quick first cut, I went ahead and tweaked this to talk MQTT.  

Protocol description coming soon...
