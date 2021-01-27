from mcpi .minecraft import Minecraft
pe = Minecraft.create()

x,y,z = pe.player.getTilePos()
for i in range(20):
    pe.setBlock(x,y-1,z+i,57)