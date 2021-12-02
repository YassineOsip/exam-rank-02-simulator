import time
animation = "|/-\\"
idx = 0
ct = 10
while ct:
    print(animation[idx % len(animation)],end="\r")
    idx += 1
    time.sleep(0.1)
    ct -= 1 
