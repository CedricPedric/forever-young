from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
e = 11
d = 10
for a in range(5):
    d = d - 2
    e = e - 2
    robotArm.grab()
    for c in range(e):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(d):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
