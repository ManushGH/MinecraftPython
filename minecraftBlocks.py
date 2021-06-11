from mcpi.minecraft import Minecraft
from mcpi import block
import random

mc = Minecraft.create("localhost", 4711)
myId = mc.getPlayerEntityId("_Karkil_")
myPos = mc.entity.getPos(myId)
x = myPos.x
y = myPos.y
z = myPos.z
mc.setBlocks(x,y,z,x+100,y+2,z+100, block.DIRT)