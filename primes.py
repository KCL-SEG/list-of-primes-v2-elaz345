"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be positive.")
    list = []
    num = 2

    while len(list) < number_of_primes:
        is_prime = all(num % prime != 0 for prime in list)

        if is_prime:
            list.append(num)

        num += 1

    return list