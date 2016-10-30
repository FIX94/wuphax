
with open('00000001.app', 'rb') as appfile:
    with open('boot.dol', 'rb') as bootfile:
        appfile.seek(0, 2)
        appfilesize = appfile.tell()
        appfile.seek(0, 0)
        print("App size : " + hex(appfilesize))
        bootfile.seek(0, 2)
        bootfilesize = bootfile.tell()
        bootfile.seek(0, 0)
        print("Boot size : " + hex(bootfilesize))
        if(bootfilesize > appfilesize):
            print("boot.dol too big to be injected!")
        else:
            with open('boot.app', 'wb') as outfile:
                print("injecting boot.dol into 00000001.app")
                outfile.write(bootfile.read(bootfilesize))
                appfile.seek(bootfilesize,0)
                outfile.write(appfile.read(appfilesize-bootfilesize))
                print("Done!")
