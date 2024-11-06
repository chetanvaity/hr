
def getAnagrams(inL):
    mA = {} # map of anagrams
    for w in inL:
        sortedW = sortW(w)
        if mA.get(sortedW) is not None:
            if w not in mA[sortedW]:
                mA[sortedW].append(w)
        else:
            mA[sortedW] = [w]
    for k in mA.keys():
        if len(mA[k]) > 1:
            print mA[k]

def sortW(word):
    return ''.join(sorted(word))
        

inList = ['ear', 'era', 'mug', 'gum', 'are', 'ear', 'sit']
getAnagrams(inList)


# StreamSets
 
// Design APIs for a simple in memory cache and implement it
// Assume it is a library which will be used by many users for various use-cases


# {'aId1' -> {'k1' -> 'v1', ...}, 'aId2' -> map, ...}
store = {}

# Get - given k return v
def getItem(aId, k):
    aMap = store.get(aId)
    return aMap[k] # TBD: error catching
    
# Set
def setItem(aId, k, v):
    aMap = store.get(aId)
    aMap[k] = v
    return

# Init Account
def initAccount():
    # generate aId
    if (store.get(aId) is None):
        store[aId] = {}
    else
        # already exists!
        pass
    return aId
