from mcpi .minecraft import Minecraft
pe = Minecraft.create()
import random,time

while True:
    x,y,z = pe.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+20
    pe.spawnEntity(x+a,y,z+b,36)
    time.sleep(0.001)