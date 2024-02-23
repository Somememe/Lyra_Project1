from random import random
from time import sleep

with open("dummy.csv", 'a') as file:
        file.write("ax,ay,az,gx,gy,gz,t\n")

for i in range(100):
    ax, ay, az = random(), random(), random()
    gx, gy, gz = random(), random(), random()
    t = random()
    with open("dummy.csv", 'a') as file:
        file.write(f"{ax},{ay},{az},{gx},{gy},{gz},{t}\n")
    sleep(2)
