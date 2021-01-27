from mcpi .minecraft import Minecraft
pe = Minecraft.create()
x,y,z = pe.player.getTilePos()
number = 1
for j in range(8):
    for i in range(number):
        pe.spawnEntity(x,y,z,60)
    number = number*2
    pe.postToChat("生成了"+str(number)+"之蠹魚")