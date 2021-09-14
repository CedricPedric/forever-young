from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
counter = 0
for a in range(9):
    robotArm.moveRight()
while counter <=8:
    robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
    print(color)
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
        counter = counter + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
