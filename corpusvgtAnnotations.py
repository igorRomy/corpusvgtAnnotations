import string

import pympi.Elan
import os
import sys

wordsDict = {}

def getWordsOfTiers():
    print("entered")
    global wordsDict
    eaf_obj = pympi.Elan.Eaf()

    for filename in os.listdir(r"C:\Users\user\Documents\eafFiles"):
        print(filename)
        usedFile = r"C:\Users\user\Documents\eafFiles\\" + filename
        pympi.Elan.parse_eaf(usedFile, eaf_obj)

        for i in eaf_obj.tiers["Vertaling i2"]:
            if isinstance(i, dict):
                for i2 in i.values():
                    if len(i2) > 2:
                        words = i2[2].split()
                        for i3 in words:
                            i3 = i3.translate(str.maketrans('', '', string.punctuation)).casefold()
                            if i3 in wordsDict:
                                wordsDict[i3] += 1
                            else:
                                wordsDict[i3] = 1
        for i in eaf_obj.tiers["Vertaling i1"]:
            if isinstance(i, dict):
                for i2 in i.values():
                    if len(i2) > 2:
                        words = i2[2].split()
                        for i3 in words:
                            i3 = i3.translate(str.maketrans('', '', string.punctuation)).casefold()
                            if i3 in wordsDict:
                                wordsDict[i3] += 1
                            else:
                                wordsDict[i3] = 1
    import operator
    sortedDict = sorted(wordsDict.items(), key=operator.itemgetter(1))
    sortedDict.reverse()
    print(sortedDict)
if __name__ == '__main__':
    getWordsOfTiers()
