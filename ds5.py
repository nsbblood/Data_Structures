#linear search

dataList=[0,3,5,11,14,16,22,25,28,30,4,12,23]

ITEM=11

def search(item,listy):
    for element in listy:
        if element==item:
            return True
    return False

print(search(ITEM,dataList))