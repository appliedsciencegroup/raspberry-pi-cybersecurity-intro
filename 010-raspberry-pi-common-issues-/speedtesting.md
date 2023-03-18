## Home Network Speedtesting

# Ethernet Test - Raspberry Pi 3 B+

To figure out the bandwidth (which is) for the Raspberry Pi, we're going to use a utility called iPerf

First, let's install it. Open up Terminal and enter

1. `sudo apt-get install iperf3`

Install iPerf on your Mac using homebrew

2. 'brew install iperf3'

3. Make sure the Raspberry Pi and your computer are both connected via ethernet

Next, we want to run iPerf3 in server mode

4. 'iperf3 -s' 

And on the Pi, we want to run it in client mode. 

5. 

Here you can see the ethernet bandwidth is
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   112 MBytes  94.3 Mbits/sec    0             sender
[  5]   0.00-10.05  sec   112 MBytes  93.5 Mbits/sec                  receiver

<img src="./gifs/iperf-pi4-bandwidth-test.gif" width="50%" height="">


#Ethernet Test - Raspberry Pi 4

You can just take the SD card out of your Pi 3, and insert it in to a Pi 4. Here's the results we got there:

1. `iperf3 -c 192.168.1.XXX`

[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   899 MBytes   754 Mbits/sec    0             sender
[  5]   0.00-10.04  sec   897 MBytes   749 Mbits/sec                  receiver

<img src="./gifs/iperf-pi3b+-bandwidth-test.gif" width="50%" height="">


#Wireless Test - Raspberry Pi 3B+

1. Download iPerf for your mobile device [here](https://iperf.fr/iperf-download.php)
    - [Apple iOS Store link](https://apps.apple.com/us/app/he-net-network-tools/id858241710)
    - [Android Google Play Store Link](https://play.google.com/store/apps/details?id=net.he.networktools)

2. Reboot your QERPI and connect to it's Wireless guest network.

Now, run the iPerf server on the Pi

3. 'iperf3 -s'

4. run iperf 3 -c 192.168.1.XXX (address of Pi Wifi)

Accepted connection from 10.10.50.50, port 63191
[  5] local 192.168.1.101 port 5201 connected to 10.10.50.50 port 63192
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec  1.45 MBytes  12.1 Mbits/sec                  
[  5]   1.00-2.00   sec  1.57 MBytes  13.2 Mbits/sec                  
[  5]   2.00-3.00   sec  1.40 MBytes  11.8 Mbits/sec                  
[  5]   3.00-4.00   sec  1.50 MBytes  12.5 Mbits/sec                  
[  5]   4.00-5.00   sec  1.20 MBytes  10.0 Mbits/sec                  
[  5]   5.00-6.00   sec  1.31 MBytes  11.0 Mbits/sec                  
[  5]   6.00-7.00   sec  1.49 MBytes  12.5 Mbits/sec                  
[  5]   7.00-8.00   sec  1.50 MBytes  12.6 Mbits/sec                  
[  5]   8.00-9.00   sec  1.49 MBytes  12.5 Mbits/sec                  
[  5]   9.00-10.00  sec  1.43 MBytes  12.0 Mbits/sec                  
[  5]  10.00-10.86  sec  1.37 MBytes  13.4 Mbits/sec                  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.86  sec  15.7 MBytes  12.1 Mbits/sec                  receiver


#Wireless - Pi4
>Now, do the same thing but make sure you update the IP address

Accepted connection from 10.10.50.50, port 63141
[  5] local 192.168.1.113 port 5201 connected to 10.10.50.50 port 63142
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec   460 KBytes  3.76 Mbits/sec                  
[  5]   1.00-2.00   sec   373 KBytes  3.06 Mbits/sec                  
[  5]   2.00-3.00   sec   380 KBytes  3.12 Mbits/sec                  
[  5]   3.00-4.00   sec   198 KBytes  1.62 Mbits/sec                  
[  5]   4.00-5.00   sec   621 KBytes  5.09 Mbits/sec                  
[  5]   5.00-6.00   sec  1.37 MBytes  11.5 Mbits/sec                  
[  5]   6.00-7.00   sec  1.46 MBytes  12.2 Mbits/sec                  
[  5]   7.00-8.00   sec  1.32 MBytes  11.1 Mbits/sec                  
[  5]   8.00-9.00   sec  1.58 MBytes  13.2 Mbits/sec                  
[  5]   9.00-10.00  sec  1.57 MBytes  13.2 Mbits/sec                  
[  5]  10.00-10.28  sec   520 KBytes  15.1 Mbits/sec                  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.28  sec  9.79 MBytes  7.99 Mbits/sec                  receiver


