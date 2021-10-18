# Raspberry Pi Halloween Motion Detection
This project uses Python 3.7 but most other versions of Python will likely work. This also uses a simple stock installation of Rasbian.  I also installed Jupyter Notebook on the Raspberry Pi for ease in development.

This project uses 120 AC voltage which will give more flexibility on the devices that can be switched on.  If you're not comfortable with AC high voltage then you can alternatively substitute low voltage to be passed through the relay.

## Required Components
* Raspberry Pi 4
* PIR (Passive Infrared sensor) - https://www.amazon.com/dp/B00JOZTAC6
* 2 Channel Relay.  This relay only supports 10A passthru so make sure you're not running something large (e.g. vacuum or toaster) through it.  LED lights are probably what you should use. - https://www.amazon.com/dp/B00E0NTPP4
* 22 AWG jumper cables.  Use 22 AWG for power.  You can go smaller for the signial wire and use 24 AWG but if you already have the 22 AWG wire then that will work perfectly fine. - https://www.amazon.com/dp/B07XMHHRDY
* Python 3.7 (earlier versions of Python will likely work just fine)
* Jupyter Notebook (optional if you want to test different Python code)
* External speakers
* 2 x 15A recepticals.  One will be used as the 'always hot' power source for the RPi and the external speakers.  The second receptical will be the 'relay receptical' and is to be switched on/off via the relay.  The relay receptical will have the tab removed between the hot side screws to create two independent plugs that can be switched on/off using the two difference channels on the relay.  You can then connect a power strip if you want to connect more devices (e.g. more lights).
* 2'-3' of 14AWG electrical wire.  Note, 14AWG is readily available in the electrical section of any home improvement store.  The 14AWG wire can support 15 amps but the relay I use can only support 10 amps.  It never hurts to go a size larger for the wire.  It also fits nicely into the recepticals and will also fix snugly into the realy.  You can add an in-line fuse if for some wild reason you think you're going to be pulling more than 10 amps and you want to protect the relay.


# Instructions
* Install just a stock version of Rasbian on the RPi
* Connect RPi periphrials (PIR, relay)
* Install Jupyter Notebook (or other editing tool, or simply use a stock text editor)
* Construct a power distribution and relay box.  This will house the PIR, relay, RPi, relay receptical, and the hot receptical.  I simply built a wooden box to hold everything.
* Construct the Halloween decorations.

The simpliest way to execute the program is to go into the `halloween` directory and execute the following function: `python3.7 main.py`

If you are happy with the code you can run the program as a background process.  Doing this will allow you to log out of the RPi.

`nohup python3.7 main.py &`

Executing the Python file will create a log file called `halloween.log` that will timestamp every motion detection.

If you want to have the program start as a service when booting the RPi it will take a couple more steps.  Setting up a service will start the script 
```
# Use a text editor to create the following file
# sudo vi /etc/systemd/system/halloween.service

[Unit]
Description=Runs Halloween Project

[Service]
ExecStart=/home/rasberrypi/main.sh start


[Install]
WantedBy=multi-user.target
```

To enable the service on boot:
`sudo systemctl enable halloween`

Then to manually start the `halloween` service execute the following command:
`sudo systemctl start halloween`

Then to stop the service execute the following command:
`sudo systemctl stop halloween`
