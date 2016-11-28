# wuphax v1.1
Hacking the vwii side of the wiiu using iosuhax and wupclient

# Usage
Grab the current elf release from the releases tab.  
Download the [hackmii installer](https://bootmii.org/download/) and put only the boot.elf from that zip on your sd card root.  
Make sure to unplug any and all usb devices before following any of these steps.  
Put the wuphax.elf into your wiiu/apps folder on your sd card and run it in homebrew launcher.  
Press A to back up your current mii channel and inject it with wuphax.  
After the wiiu restarted, go into wii mode and run mii channel, install homebrew channel from there.  
To restore the mii channel just run the elf again and press B this time.  

# Dependencies
To properly compile this project yourself you will need the latest libiosuhax from dimok789's github.  