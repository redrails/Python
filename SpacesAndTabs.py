# Made by redrails/ihtasham.

import sys
from copy import *


def spacesToTabs(reqFile, step):

    randFN = reqFile+".tabs"
    space = " "
    spaceFinder = deepcopy(space)*step

    tabReplacer = '\t'


    with open(randFN, "wt") as fout:
        with open(reqFile, "rt") as fin:
            for line in fin:
                fout.write(line.replace(spaceFinder, tabReplacer))



    print "Created new file", randFN

def tabsToSpaces(reqFile):

    randFN = reqFile+".spaces"

    tabFinder = '\t'
    spaceReplacer = "    "


    with open(randFN, "wt") as fout:
        with open(reqFile, "rt") as fin:
            for line in fin:
                fout.write(line.replace(tabFinder, spaceReplacer))



    print "Created new file", randFN


spacesToTabs("./testFile.txt", 5) # Convert spaces to tabs from testFile.txt with 5 spaces as a tab.
tabsToSpaces("./testFile.txt")    # Convert tabs to spaces, not added step but it's 4 spaces per tab by default. 
