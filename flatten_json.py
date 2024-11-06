import sys
import json

# Tested with Python 2.7
# Invoke with one argument
# eg: python flatten_json.py restaurant.json

# Collect all inner objects in this global map of lists
cLists = {}

def getFlattenedMap(m, name):
    global cLists
    _id = m["id"]
    nm = {}
    for k in m.keys():
        if (type(m[k]) is not list) and (type(m[k]) is not dict):
            nm[k] = m[k]
        elif type(m[k]) is list:
            writeList(m[k], "%s_%s" % (name, k), _id)
        elif type(m[k]) is dict:
            cName = "%s_%s" % (name, k)
            if cLists.get(cName) is None:
                cLists[cName] = []
            m[k]["id"] = _id    
            cLists[cName].append(getFlattenedMap(m[k], cName))
    return nm

        
def writeList(l, pName, _id):
    nList = []
    index = 0
    for i in l:
        if type(i) is dict:
            if i.get("id") is None:
                i["id"] = _id
            i["__index"] = index
            nList.append(getFlattenedMap(i, pName))
        else:
            nList.append(i)
        index = index + 1    
    with open("%s.json" % (pName), 'w') as lf:
        lf.write(json.dumps(nList))
        

# Main program here
with open(sys.argv[1], 'r') as f:
    s = f.read()

d = json.loads(s)
for k in d.keys():
    if type(d[k]) is list:
        writeList(d[k], "o_%s" % (k), "NA")
    else:
        print 'not list' + k
        sys.exit(1)
    for childName in cLists.keys():
        writeList(cLists[childName], childName, "NA")
