"""
my attempt at making addition
"""
def right(r):
    val = r.count(0)
    if val ==0:
        pass
    else:
        for i in range(val):
            r.remove(0)
        for j in range(val):
            r.insert(0,0)

    for i in range(3):
        if r[3-i]==r[2-i]:
            r[3-i]*=2
            del r[2-i]
            r.insert(0,0)
    return r
    
def left(r):
    val = r.count(0)
    if val ==0:
        pass
    else:
        for i in range(val):
            r.remove(0)
        for j in range(val):
            r.append(0)

    for i in range(3):
        if r[i]==r[i+1]:
            r[i]*=2
            del r[i+1]
            r.append(0)
    return r

def down(r):
    val = r.count(0)
    if val ==0:
        pass
    else:
        for i in range(val):
            r.remove(0)
        for j in range(val):
            r.insert(0,0)

    for i in range(3):
        if r[3-i]==r[2-i]:
            r[3-i]*=2
            del r[2-i]
            r.insert(0,0)
    return r
    
def up(r):
    val = r.count(0)
    if val ==0:
        pass
    else:
        for i in range(val):
            r.remove(0)
        for j in range(val):
            r.append(0)

    for i in range(3):
        if r[i]==r[i+1]:
            r[i]*=2
            del r[i+1]
            r.append(0)
    return r