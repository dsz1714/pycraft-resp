import easygui
import time
import random
print("PyCraft Execute Disclaimer v3.6.0 for pycraft 1.2.0 exp-snp")
patched=False
while True:
    c=easygui.buttonbox("Select Options",choices=['Patch','Generate','Exit'])
    if c=='Patch':
        time.sleep(1)
        print("Successfully patched with PyCraft 1.2.0 exp-snp!")
        patched=True
    elif c=='Generate':
        if patched:
            print("Connecting to api.pycraft.net...")
            print("Connecting to verify.pycraft.net...")
            time.sleep(2)
            print("With opened api.core.pycraft.net/keys.html")
            time.sleep(1)
            print("Reading coreloads.pycraft.net/core.php?=0910...")
            time.sleep(2)
            print("Generating hs5 key chains...")
            print("Patched: verification.gamefun.com/pycraft")
            time.sleep(3)
            print("Calculating avalible keys...")
            print("Waiting...")
            time.sleep(1)
            print("Avalile key:",end='')
            print(18028922)
        else:
            print(random.randint(10000000,99999999))
    else:
        break
