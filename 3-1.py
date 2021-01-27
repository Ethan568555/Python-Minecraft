from mcpi .minecraft import Minecraft
pe = Minecraft.create()

while True:
    hits = pe.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z, = a.pos.x,a.pos.y,a.pos.z
        block = pe.getBlock(x,y,z)
        pe.postToChat("you hit"+str(block))