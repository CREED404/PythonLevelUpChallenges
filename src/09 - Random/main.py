from collections import defaultdict
import random

def roll_dice(*arg):
    number_of_tests = 1_000_000
    dices = []

    for dice in arg:
        tmp = []
        for side in range(1, dice+1):
            tmp.append(side)
        dices.append(tmp)

    tests = defaultdict(int)
    for _ in range(0, number_of_tests+1):
        tmp = []
        for x in dices:
            tmp.append(x[random.randrange(0, len(x))])
        tests[sum(tmp)] += 1

    probabilities = sorted(tests.items(), key=lambda x: x[0])
    for probability in probabilities:
        print(f"{probability[0]} : {(probability[1]/number_of_tests)*100:.2f}%")
