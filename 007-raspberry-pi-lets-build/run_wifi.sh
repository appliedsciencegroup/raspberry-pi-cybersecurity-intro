#!/bin/sh

# Pause for 1 second
sleep 1
# Move to your root directory
cd /
# Move to the directory where QERPI is installed
cd /home/pi/qerpi
# Run the ap.py script
sudo python3 ap.py &
cd /
