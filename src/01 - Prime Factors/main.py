def get_prime_factors(number):
  factors = []

  divisor = 2
  while number != 1:
    if number % divisor == 0:
      factors.append(divisor)
      number = number // divisor
    else:
      divisor += 1

  print(factors)