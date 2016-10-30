# wuphax
Hacking the vwii side of the wiiu using iosuhax and wupclient

# Usage
Make sure to have iosuhax with only wupserver enabled set up already, this version can be found in my fork of iosuhax.  
Download the release of this project and extract it into a new folder.  
Download the hackmii installer and put its boot.elf on your sd card.  
To use this start up iosuhax and edit the wiiu ip in wupclient.py (line 29) to match the one you have.  
After that run backup.py, this should give you a 00000001.app if everything went well.  
Run injectdol.py, this should give you a boot.app.  
Now just run writedol.py and wait for it to upload the new executable.  
After that is done, shut down your wiiu, unplug its power, replug it and go into wii mode.  
In wii mode, run the mii channel, this should start up the boot.elf on your sd card root, install homebrew channel from here.  
To restore your original mii channel, start up iosuhax again and run restore.py.  
After that is finished you can just shut down your wiiu again, unplug the power and replug, after this point your mii channel should be back to normal.  