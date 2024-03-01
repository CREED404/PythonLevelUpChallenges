def allPrimesUpTo(num):
    factorsList = [1, ]
    for number in range(2, num):
        sqr = int(number ** 0.5)+1
        for numberx in factorsList:
            if number % numberx == 0 and numberx not in (number, 1):
                break
            if numberx > sqr and sqr > 1:
                factorsList.append(number)
                break
        else:
            #if number not in factorsList:
            factorsList.append(number)
    return factorsList

def get_prime_factors(num):
    if num == 1:
        return [1]
    elif num <= 0:
        return 0
    
    primeList = allPrimesUpTo(num+1)[1:]
    pointer = 0
    result = []

    while True:
        if (num) in primeList:
            result.append(num)
            break

        elif (num // primeList[pointer]) == 1:
            result.append(primeList[pointer])
            break

        elif (num % primeList[pointer]) == 0:
            result.append(primeList[pointer])
            num = num //primeList[pointer]
            print(result)
            continue

        else:
            pointer += 1
    
    return result
