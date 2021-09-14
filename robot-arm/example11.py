from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:

loopA = 0 # Waarde van while loop
positie = 1 # Waarde van de positie van het blokje waar de grijpklauw is gebleven
totaalPositie = 10 # Waarde van het aantal posities

while loopA <= 8: # Het blokje begint op 1 dus als er meer dan 8 loops zijn geweest stop het programma
    loopB = 0 # Waarde van b is 0 wordt elke loop 0
    loopC = 0 # Zelfde als b
    
    robotArm.grab()
    color = robotArm.scan()
    afstand = totaalPositie - positie # Som van het aantal posities wat de klauw moet gaan 10 - positie
    if color == 'red': # Als de kleur rood is voert het progamma dit uit
        #print(afstand) 
        while loopB != afstand: # Het progamma blijft naar rechts gaan todat het gelijk is aan de afstand die het moest leggen
            robotArm.moveRight()
            loopB = loopB + 1
        robotArm.drop() # Het laat de kubus vallen
        positie = positie + 1 # De positie verplaatst anders grijpt de klauw niks
        afstand = afstand - 1 # De afstand wordt wel minder want de klauw moet minder ver heen dan terug
        #print(afstand)
        while loopC != afstand: # De klauw beweegt de terugweg dus heen -1 stap
            robotArm.moveLeft()
            loopC = loopC + 1
    else: # Als het niet 'red' is dan laat hij de kubus vallen en gaat het naar rechts
        robotArm.drop()
        robotArm.moveRight()
        positie = positie + 1 # De positie gaat hier ook vooruit

    loopA = loopA + 1 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()