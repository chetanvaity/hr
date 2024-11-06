


def getAnagrams(inL):
    mA = {} # map of anagrams
    sortedW = sortW(w)
    for sortedW in inL:
        if mA.get(sortedW) is not None:
            mA.append(w)
        else:
            mA[sortedW] = [w]
    for k in mA.keys():
        print mA[k]


inList = ['ear', 'era', 'mug', 'gum', 'are', 'ear', 'sit']
getAnagrams(inList)
