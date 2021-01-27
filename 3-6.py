from mcpi .minecraft import Minecraft
pe = Minecraft.create()

x,y,z = pe.player.getTilePos()
for i in range(20):
    pe.setBlock(x+i+1,y-1,z+i,57)
    pe.setBlock(x+i+2,y-1,z+i,57)
    pe.setBlock(x+i+3,y-1,z+i,57)