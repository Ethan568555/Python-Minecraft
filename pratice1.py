from mcpi .minecraft import Minecraft
pe = Minecraft.create()

import random
while True:
    x,y,z=pe.player.getTilePos()
    color = random.randrange(0,9)
    pe.setBlock(x,y,z-1,38,color)
    pe.setBlock(x,y,z+1,38,color)
    pe.setBlock(x-1,y,z,38,color)
    pe.setBlock(x+1,y,z,38,color)
    