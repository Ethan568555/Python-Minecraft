def plantTree(x,y,z):
    pe.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    pe.setBlocks(x,y,z,x,y+4,z,17)
from mcpi .minecraft import Minecraft
pe = Minecraft.create()
x,y,z = pe.player.getTilePos()
'''
for i in range(0,50,5):
    plantTree(x+i,y,z)
'''
for i in range(10):
    for j in range(8):
        for k in range(10):
            plantTree(x+i*5,y+j*8,z+k*5)