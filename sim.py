"""
Does a simulation of the monty hall problem.
"""
import sys
import math
import random

def Run(switch):
    """
    Do the simulation.
    """
    doors = [0,1,2]
    car = int(math.floor(random.random() * 3))
    pick = int(math.floor(random.random() * 3))

    if not switch:
    # case no switch
        if car == pick and not switch:
            return 1
        else:
            return 0
    
    # case switch

    # doors for the host to open 
    fairgame = [i for i in doors if (i != car and i != pick)]
    hostdoor = random.choice(fairgame)

    finalchoice = [i for i in doors if i != hostdoor and i != pick]
    if finalchoice[0] == car:
        return 1
    return 0

    





if __name__ == "__main__":
    if sys.argv[1] == "switch":
        switch = True
    else:
        switch = False
    sum = 0
    for i in range(100000000):
        sum += Run(switch)
    print 1.0 * sum / 100000000
