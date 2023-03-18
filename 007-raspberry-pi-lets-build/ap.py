#---------- Import all the stuff we need ----------#

# Lots of code that we need to create a wireless access point already exists.
# First, we're going to LOOK in the package PyAccessPoint and then IMPORT the program called 'pyaccesspoint'
# This will create hotspot named "MyAccessPoint" on wlan0 with "1234567890" password.
# Learn more, here: https://github.com/Goblenus/pyaccesspoint
from PyAccessPoint import pyaccesspoint

# Next, we're going to import three programs: Image, ImageDraw and ImageFont from PIL (Python Image Library)
#Learn more, here: https://github.com/python-imaging/python-imaging.github.io
from PIL import Image, ImageDraw, ImageFont

# Here, we're importing the QR Code generation package, and all of it's programs.
import qrcode

#This package lets us create a new process, which is an application, within our application.
import subprocess

# This package lets us find out the time in a variety of formats.
import time

# This module implements pseudo-random number generators for various distributions.
import random

# Wireless Access Point Settings

# Here we are setting the wlan interface, this is your wireless interface.
set_wlan = "wlan0" 

# Here we are setting the inet interface, this is your ethernate interface.
set_inet = "eth0"

#---------- Name of the Guest Wireless Network you want to create ----------#
set_ssid = "QERPI_guest"

# Sets the initial password for your wireless network. 
set_pass = ""

# Sets the IP address of the router.
set_ip = "10.10.50.1"

# Sets the Subnet Mask, which is the number of IP addresses that it will make available in a network.
# Systems in the same subnet can communicate with eachother, ones on different subnets require a router.
# There are 255.255.255.255 combinations, and so this says the first 3 are full, so make new IP addresses where the last four digits are from 0 to 255.
set_netmask = "255.255.255.0"

# This means create the QR code and name it 'qr_code.png'
file_name_qr = 'qr_code.png'

# This means save the QR code, in the /var/www/html/ directory and rename it to 'qr_www.png'
# This is the directory of the Apache webserver
file_name_www = '/var/www/html/qr_www.png'

# This is the filename for the text data wifi connection
wifi_txt = '/var/www/html/wifi.txt'

# the variable that determines the stage of the main program
state = 0

#---------- How often the network password (and QR code) changes (in seconds). ----------#
# 5 minutes = 60 seconds * 5 = 300 seconds
time_QR_gen = 86400 #1200
#39600
count_timer = 0
timer_cooldown = 60

offset_y_txt = 320 

# This creates the QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

# Create a function called pass_word using words in the file dictionary.txt that are at last 6 characters long
def pass_word(min_length=6, filename="dictionary.txt"):
	# If you want something 6 characters long, you need to make it 6 + 1 characters long
	min_line_length = min_length + 1
	max_line_length = min_line_length + 4
	# Read dictionary.txt line by line
	with open(filename) as wordbook:

# ----		# This picks two words that are greater than the minimimum line length

		large_words = [line for line in wordbook if (len(line) >= min_line_length and len(line) < max_line_length)]
	# This picks a random word, sorted by length

	word_1 = random.choice(large_words).rstrip('\n')
	word_2 = random.choice(large_words).rstrip('\n')

	# Pick a random number from 0 to 9 (in increments of 1)
	number_1 = random.randrange(0, 9, 1)
	number_2 = random.randrange(0, 9, 1)

	# Add the two words + two numbers together
	password = word_1 + word_2 + str(number_1) + str(number_2)
	# Returns the password
	return password

# This creates the wireless acces point object with the above variables
access_point = pyaccesspoint.AccessPoint(wlan=set_wlan, inet=set_inet, ip = set_ip, netmask=set_netmask, ssid=set_ssid)

# This is how you stop the wireless access point
access_point.stop()

# This creates the font style and size object
font_bold = ImageFont.truetype("DejaVuSans-Bold.ttf", size=12)
font = ImageFont.truetype("DejaVuSans.ttf", size=12)

#---------- This is the main program ----------#
# This creates an infinite loop from the start

while True:
	# There is a 1 second delay before getting started. This is used to determine the initial state of the machine.
	time.sleep(1)

	# Initializes the state
	if state == 0:

		# ------ dictionary-based password function call from several words
		#------- minimum word length = 6 
		set_pass = pass_word(6)
		
		# Creates the background image, 320x480 and black. We'll add the text later.
		bg_img = Image.new('RGBA', (320, 480), 'black')
		
		# Creates an object that can be used to draw on.
		bg_draw = ImageDraw.Draw(bg_img)

		# The text that will be displayed below the image
		text_SSID = '        SSID:'
		text_Password = 'Password:'
		
		# Getting in pixels the total length of the text of the word password and password values.
		width_txt, height_txt = bg_draw.textsize(text_Password, font_bold)
		width_txt_pass, height_txt_pass = bg_draw.textsize(set_pass, font)
		
		# Offset calculation to center the text
		offset_x_txt = int((320 - (width_txt + width_txt_pass+10))/2)	
		
		# Insert text, but offset it (X,Y) when placing it on the background

		bg_draw.text((offset_x_txt, offset_y_txt), text_SSID, font=font_bold)
		bg_draw.text((offset_x_txt+ width_txt+10, offset_y_txt), set_ssid, font=font)
		bg_draw.text((offset_x_txt, offset_y_txt+20), text_Password, font=font_bold)
		bg_draw.text((offset_x_txt + width_txt+10, offset_y_txt+20), set_pass, font=font)

		text_Time = "Time remaining:"
		w_text_Time, h_text_Time = bg_draw.textsize(text_Time, font_bold)
		offset_x_text_Time = int((320 - w_text_Time)/2)
		bg_draw.text((offset_x_text_Time, 380), text_Time, font=font_bold)
		
		text_full_timer = "24:00 until password resets"
		w_text_full_timer, h_text_full_timer = bg_draw.textsize(text_full_timer, font)
		offset_x_text_full_timer = int((320 - w_text_full_timer)/2)
		bg_draw.text((offset_x_text_full_timer, 400), text_full_timer, font=font)
		
		text_qerpi = "qerpi.com"
		w_text_qerpi, h_text_qerpi = bg_draw.textsize(text_qerpi, font_bold)
		offset_x_text_qerpi = int((320 - w_text_qerpi)/2)
		bg_draw.text((offset_x_text_qerpi, 460), text_qerpi, font=font_bold)

		# Assigns the randomly generated password to the Access Point
		access_point.password = set_pass

		# Tells the Access Point to start
		access_point.start()

		# Changes the state from 0 to 1
		state = 1

	# This is the main program. It's a loop that runs whenever the state = 1
	elif state == 1:

		# Check if the Access Point is running
		if access_point.is_running():		
			# Show in the terminal that the access point is running, and what the password is.
			# This is useful for debugging
			print ('Starting AP network:       ', set_ssid)
			print ('Starting AP with password: ', set_pass)
			print ('********************************************')
			
			# Remember what time the access point started
			# Because every (x) minutes, we have to change the QR code
			time_start = time.time()
			
			timer_start = time_start

			# This takes the raw data from the access point (password) and creates a QR code.
			# A QR code is really a string of text, for example: WIFI:S:QERPI_guest;T:WPA;P:NVDyJ6jHXBRrWD3q;;
			# And then encoded as an image
			qr_data='WIFI:S:'+ set_ssid +';T:WPA;P:' + set_pass + ';;'

			# Clear the QR code object
			qr.clear()

			# Add the newly prepared data to the QRcode object
			qr.add_data(qr_data)

			# Make the QR code automatically fit
			qr.make(fit=True)
			
			# Create the QR code, with white squares on a black background.
			img = qr.make_image(fill_color="white", back_color="black")
						
			# Get size QR code picture
			width_img, height_img = img.size
			
			# Offset calculation to center the image
			offset_x_qr = int((320 - width_img)/2)
			offset_y_qr = 5

			# This is the offset (X, Y) when we place the QR code picture on the background picture
			# This is specifically offset to be in the center of the LCD screen we recommend you use.
			offset_qr_picture = (offset_x_qr, offset_y_qr)

			# Place the image of the QR code on the background, with an offset
			bg_img.paste(img, offset_qr_picture)

			# Save the QR code image with this file name
			bg_img.save(file_name_qr)
			
			# Save the QR code image with this file name (for the web)
			img.save(file_name_www)
			
			# Save the WIFI Network Name (SSID) and Password to a text file (for the web)
			try:
				f = open (wifi_txt, "w+")
				f.write(set_ssid + '\n' + set_pass)
				f.close()
			except:
				pass
			
			# Run a subprocess, start the image viewer (FEH) and open the image fullscreen
			p = subprocess.Popen(['feh', file_name_qr, '-FNY'])			
			
			# Set the new state to 2
			state = 2
		
		#If the Wireless AP does not start, show this message in the terminal
		else:
			print ("Please wait for the WiFi access point to start up...")
			time.sleep(5)
	
	# Check what the password refresh time is
	elif state == 2:
	
		# Wait for that amount of time
		if (time.time() - time_start >= time_QR_gen):			
	
			# When you reach that time, stop
			access_point.stop()
			
			count_timer = 0
			
			# Now set the new state to 3
			state = 3		
		elif (time.time() - timer_start >= timer_cooldown):
			timer_start = time.time()
			count_timer += 1
			remaining_time = time_QR_gen - timer_cooldown * count_timer			
			timer_h = int(remaining_time / 3600)			
			timer_min = int((remaining_time - timer_h*3600) / 60)
			str_h = '%02d' % (timer_h)
			str_min = '%02d' % (timer_min)
			text_24h = " until password resets"
			text_full_timer = str_h + ':' + str_min + text_24h
						
			bg_draw.rectangle(((0, 400), (320, 420)), fill="black")
			w_text_full_timer, h_text_full_timer = bg_draw.textsize(text_full_timer, font)
			offset_x_text_full_timer = int((320 - w_text_full_timer)/2)
			bg_draw.text((offset_x_text_full_timer, 400), text_full_timer, font=font)
			bg_img.save(file_name_qr)
			
			p.kill()
			p = subprocess.Popen(['feh', file_name_qr, '-FNY'])
		
	# Close the existing QR code
	elif state == 3:	
	
		# Check if the access point is stopped
	
		if (access_point.is_running() == False):
	
			# If it's stopped, print this to the terminal (for debugging)
			print ('The WiFi access point is now refreshing')		
	
			# Kill the image viewer subprocess
			p.kill()
	
			# Set the new state to 0
			state = 0
