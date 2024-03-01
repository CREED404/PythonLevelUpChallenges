# input          : [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# find 2         : [[0, 0, 1], [0, 1], [1, 1]]
# find [1, 2, 3] : [[0, 0], [1]]


def index_all(theList: list, value):
    indexes = []
    value   = value
    level   = 0
    tmp=[]
    def recursion(listOrValue: list, i=None):
        nonlocal indexes
        nonlocal level
        nonlocal tmp
        if listOrValue == value:
            #print(f"{index=}, {level=}, {listOrValue=}")
            indexes.append(tmp.copy())
            print("now: ", tmp)
            return
        if isinstance(listOrValue, list):
            level+=1
            if level != len(tmp):
                tmp.append(0)
            for i, _list in enumerate(listOrValue):
                tmp[level-1]=i
                print("tmp: ", tmp)
                recursion(_list, i)
            level-=1
            tmp=tmp[0:-1]
    recursion(theList)
    return indexes
