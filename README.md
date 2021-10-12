# Raspberry Pi Halloween Motion Detection
This uses Python 3.7 but other versions of Python will likely work. This also uses a simple stock installation of Rasbian.  I also installed Jupyter Notebook on the Raspberry Pi for ease in development.

This project uses 120 AC voltage which will give more flexibility on the devices that can be switched on.  If you're not comfortable with AC voltage then you can alternatively substitute low voltage to be passed through the relay.

## Required Components
* Raspberry Pi 4
* PIR (Passive Infrared sensor) - https://www.amazon.com/dp/B00JOZTAC6
* 2 Channel Relay.  This relay only support 10A passthru so make sure you're not running something large like a vacuum through it.  LED lights are probably what you should use. - https://www.amazon.com/dp/B00E0NTPP4
* 22 AWG Jumper cables.  I recommend 22 AWG for power.  You can also use the 22 AWG for the periphrial signal as well. - https://www.amazon.com/dp/B07XMHHRDY
* Python 3.7 (other versions of Python will likely work just fine)
* Jupyter Notebook
* 2 x 15A recepticals.  One as the source power for the RPi to connect to.  The second to be switched on/off via the relay.
* 5'-10' of 14AWG electrical wire.  Note, 14AWG is readily available in the electrical section of any home improvement store and it doesn't hurt to go slightly larger.  The 14AWG wire can support 15 amps but the relay I use can only support 10 amps.  So in reality 18AWG wire would be sufficient for the relay.


# Instructions
* Install Rasbian on the RPi
* Connect periphrials (PIR, relay)
* Install Jupyter (or other editing tool, or simply use the stock text editor)
