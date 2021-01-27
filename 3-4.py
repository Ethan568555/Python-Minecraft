from mcpi .minecraft import Minecraft
pe = Minecraft.create()

while True:
    hits = pe.events.pollProjectileHits()
    if len(hits) > 0 :
        a = hits[0]
        x,y,z, = a.pos.x,a.pos.y,a.pos.z
        pe = pe.createExplosion(x,y,z,power=300)