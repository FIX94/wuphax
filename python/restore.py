import wupclient

if __name__ == '__main__':
    print("Connecting to wupserver")
    w = wupclient.wupclient()
    if(w.s == None):
        print("Failed to connect to wupserver!")
        exit()
    print("Connected!")
    wupclient.w = w
    print("Mounting vWii NAND")
    ret = wupclient.mount_slccmpt01()
    if(ret != 0):
        print("Failed to mount vWii NAND!")
    else:
        print("Mounted! Navigating to mii channel folder")
        ret = w.cd("/vol/storage_slccmpt01/title/00010002/48414341/content")
        if(ret != 0):
            print("Failed to navigate to mii channel folder!")
        else:
            print("Restoring mii channel executable, this might take a while")
            ret = w.up("00000001.app")
            if(ret == 0):
                print("Success!")
            else:
                print("Failed to upload executable!")
        ret = wupclient.unmount_slccmpt01()
        if(ret != 0):
            print("Failed to unmount vWii NAND!")
        else:
            print("Unmounted vWii NAND")
    if(w.fsa_handle != None):
        w.close(w.fsa_handle)
        w.fsa_handle = None
    if(w.s != None):
        w.s.close()
        w.s = None
