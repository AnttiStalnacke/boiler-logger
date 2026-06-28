# Idea
Monitor the screw of the boiler by monitoring the 5v output of a USB charger placed in the power outlet next to the screw.

# Needs
 - Real time logging of state change on the 5v
 - Access via SSH

# Suggested platform
Rasperry Pi 5 (2 GB) which has:
 - Onboard real time clock (separate battery needed though)
 - GPIO
 - Enough compute power by far
 - WiFi and Bluetooth

Can be booted from USB and OS installed. 

# Parts list
[https://www.electrokit.com/minneskort-sdhc-32gb-med-raspberry-pi-os]
[https://www.electrokit.com/raspberry-pi-5-1gb]
[https://www.electrokit.com/natadapter-27w-usb-c-pd-raspberry-pi-5-svart]

# Running the code
Run code via uv by calling:
```uv run boiler_logger```
