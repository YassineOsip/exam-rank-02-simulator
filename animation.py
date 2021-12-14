import time
import signal
import os

global run
print("waitting for moulinette dyal jumia:%s" % os.getpid())

def animationHadler(signum, frame):
    global run
    run = False

signal.signal(signal.SIGUSR1, animationHadler)

def animate():
    animation = "|/-\\"
    idx = 0
    global run
    run = True
    while run:
        print(animation[idx % len(animation)],end="\r")
        idx += 1
        time.sleep(0.1)
animate()
