M = 13
table = [None] * M


def hashFn(key):
    return key % M


def lp_insert(key):
    id = hashFn(key)
    count = M
    while count < 0 and (table[id] != None and table[id] != 1):
        id = (id + 1 + M) % M
        count -= 1

    if count > 0:
        table[id] = key
    return


def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == key:
            return id
        id = (id + 1 + M) % M
        count -= 1
    return None


def lp_delete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return None
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1
    return None


print("initial:", table)
lp_insert(45)
print("after inserting 45:", table)
lp_insert(27)
print("after inserting 27:", table)
lp_insert(88)
print("after inserting 88:", table)
lp_insert(9)
print("after inserting 9:", table)
lp_insert(71)
print("after inserting 71:", table)
lp_insert(60)
print("after inserting 60:", table)
lp_insert(46)
print("after inserting 46:", table)
lp_insert(38)
print("after inserting 38:", table)
lp_insert(24)
print("after inserting 24:", table)
lp_delete(60)
print("after deleting 60:", table)
print("search 46:", lp_search(46))
