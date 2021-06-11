import random
import time
from mcpi import block
from mcturtle import minecraftturtle
from mcpi.minecraft import Minecraft


mc = Minecraft.create("localhost", 4711)
myId = mc.getPlayerEntityId("_Karkil_")
mc.entity.setPos(myId, 301, 80, 201)
myPos = mc.entity.getPos(myId)
x = myPos.x
y = myPos.y
z = myPos.z
lavaList = []
points = 0


def main():
    mc.postToChat("Starting the maze. You lose 2 points on mistake and gain 10 points for every checkpoint, there "
                  "are some hidden bonus points too")
    mc.setBlocks(x, y + 20, z, x + 100, y - 10, z + 100, block.AIR)
    mc.setBlocks(300, y +3 , z, 700, y + 200, z + 200, block.AIR)
    mc.setBlocks(x, y, z, x + 100, y + 2, z + 100, block.DIAMOND_BLOCK)
    mc.setBlocks(x, y + 3, z, x + 100, y + 3, z + 100, block.FENCE_NETHER_BRICK)
    mc.setBlocks(x + 1, y + 3, z + 1, x + 99, y + 3, z + 99, block.AIR)
    mc.setBlocks(x, y + 3, z + 6, x + 98, y + 3, z + 6, block.FENCE_NETHER_BRICK)
    mc.setBlocks(x+2, y + 3, z + 21, x + 99, y + 3, z + 21, block.FENCE_NETHER_BRICK)

    for i in range(305, 400, 20):
        slabs(i)
    mc.entity.setPos(myId, x + 2, y + 4, z + 3)
    mc.setBlock(401, y + 3, 205, block.GOLD_BLOCK)
    round1()
    round2()


def round1():
    global points
    lavaList.clear()
    for i in range(200):
        xLava = random.randrange(x + 3, x + 99)
        zLava = random.randrange(z + 1, z + 6)
        lavaPos = int(xLava), int(y + 2), int(zLava)
        lavaList.append(lavaPos)
        mc.setBlock(xLava, y + 2, zLava, block.LAVA_STATIONARY)
    checkpoint = False
    while not checkpoint:
        global points
        curPos = mc.entity.getPos(myId)
        if curPos.x >= 400:
            checkpoint = True
            points += 10
            mc.postToChat("Checkpoint saved")
            mc.postToChat("Points :" + str(points))
            break
        curPos = int(curPos.x), int(curPos.y), int(curPos.z)
        if curPos in lavaList:
            points -= 2
            mc.postToChat("Try again! Reset at start")
            mc.entity.setPos(myId, x + 2, y + 4, z + 3)


def round2():
    global points
    checkpoint2 = False
    bonusPoints = False
    while not checkpoint2:
        curPos = mc.entity.getPos(myId)
        bonusBlock = 400, 83, 205
        blockEvent = mc.events.pollBlockHits()
        if curPos.x <= 303:
            mc.entity.setPos(myId, 350, y+3, z+50)
            checkpoint2 = True
            mc.postToChat("End reached")
            curPos = mc.entity.getPos(myId)
            points += 10
            mc.postToChat("Points :" + str(points))
            print_name()
            break
        if 303 < curPos.x < 399:
            flying = True
            posX = 400
            posY = y+23
            posZ = z+14
            while flying:
                mc.entity.setPos(myId, posX, posY, posZ)
                posX -= 0.5
                time.sleep(0.3)
                if posX < 303:
                    flying = False
                    break
                blockEvents = mc.events.pollBlockHits()
                if len(blockEvents) > 0:
                    posY += 2
                else:
                    posY -= .1
                if not mc.getBlock(posX, posY, posZ) == 0:
                    points -= 2
                    mc.postToChat("Try again! Reset at checkpoint")
                    mc.entity.setPos(myId, 400, y + 3, 205)
                    break
        if curPos.x > 399:
            curPos2 = int(curPos.x), int(curPos.y), int(curPos.z)
            while not bonusPoints:
                if curPos2 == bonusBlock and int(len(blockEvent)) > 0:
                    mc.postToChat("Bonus points :)")
                    points += 5
                    mc.postToChat("Points: " + str(points))
                    bonusPoints = True
                else:
                    break


def print_name():
    mc.entity.setPos(myId, 350, y + 3, z + 25)
    mc.postToChat("Well Done!")
    curPos = mc.entity.getPos(myId)
    turtle = minecraftturtle.MinecraftTurtle(mc, curPos)
    turtle.penblock(block.WOOL)
    turtle.speed(10)
    turtle.up(90)
    turtle.forward(8)
    turtle.right(90)
    turtle.down(135)
    turtle.forward(5)
    turtle.up(90)
    turtle.forward(5)
    turtle.down(135)
    turtle.forward(8)
    turtle.backward(8)
    turtle.setz(234)
    turtle.forward(8)
    turtle.up(135)
    turtle.forward(10)
    turtle.down(90)
    turtle.forward(10)
    turtle.up(135)
    turtle.forward(8)
    turtle.down(135)
    turtle.forward(10)
    turtle.up(135)
    turtle.forward(8)
    turtle.setz(turtle.position.z + 2)
    turtle.sety(y + 3)
    turtle.forward(8)
    turtle.setz(turtle.position.z + 1)
    turtle.sety(y + 4)
    turtle.down(90)
    turtle.forward(4)
    turtle.up(90)
    turtle.forward(7)
    turtle.down(90)
    letter_S_z = turtle.position.z + 2
    turtle.setz(letter_S_z)
    turtle.forward(5)
    turtle.setz(letter_S_z)
    turtle.sety(y + 4)
    turtle.forward(5)
    turtle.setz(letter_S_z)
    turtle.sety(y + 7)
    turtle.forward(5)
    turtle.setz(letter_S_z)
    turtle.sety(y + 7)
    turtle.down(90)
    turtle.backward(4)
    turtle.setz(letter_S_z + 5)
    turtle.sety(y + 3)
    turtle.backward(4)
    turtle.setz(turtle.position.z + 2)
    turtle.sety(y + 3)
    turtle.backward(8)
    turtle.setz(turtle.position.z + 1)
    turtle.sety(y + 7)
    turtle.up(90)
    turtle.forward(4)
    turtle.up(90)
    turtle.backward(4)
    turtle.forward(8)


def slabs(slabX):
    mc.setBlocks(slabX, y+3, z+7, slabX, y+40, z+20, block.GLOWSTONE_BLOCK)
    slabY = random.randint(y+15, y+30)
    mc.setBlocks(slabX, slabY-5, z+7, slabX, slabY+5, z+20, block.AIR)


main()
