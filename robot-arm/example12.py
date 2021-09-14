from pygame import Color
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
a = 0
amountMoved = 0

while a < 1:
    robotArm.grab()
    amountMoved = amountMoved + 1
    color = robotArm.scan()

    if color != "" :

        for b in range(amountMoved):
            robotArm.moveRight()

        robotArm.drop()

        for c in range(amountMoved + 1):
            robotArm.moveLeft()
            c = c + 1 
    else:
        a = a + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()