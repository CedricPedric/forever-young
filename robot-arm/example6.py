from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for b in range(5):
    for a in range (6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        
    robotArm.moveRight()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
