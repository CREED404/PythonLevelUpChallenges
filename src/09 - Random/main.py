from collections import defaultdict

def roll_dice(*arg):
    number_of_tests = 1_000_000
    dices = []
    for dice in arg:
        tmp = []
        for side in range(1, dice+1):
            tmp.append(side)
        dices.append(tmp)
    #print(dices)
    tests = []
    for _ in range(0, number_of_tests+1):
        tmp = []
        for x in dices:
            tmp.append(x[random.randrange(0, len(x))])
        tests.append(sum(tmp))
    #print(tests)
    unique = defaultdict(int)
    for x in tests:
        unique[x] += 1
    #print(unique, len(tests))
    unique = sorted(unique.items(), key=lambda x: x[0])
    for x in unique:
        print(f"{x[0]} : {(x[1]/number_of_tests)*100:.2f}%")
