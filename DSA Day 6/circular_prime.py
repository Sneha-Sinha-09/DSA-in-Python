'''The number, 197, is called a circular prime because all
 rotations of the digits: 197, 971, and 719, are themselves
 prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of 
circular primes less than the given limit.'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        rotated_str = str_n[i:] + str_n[:i]
        rotated_num = int(rotated_str)
        if not is_prime(rotated_num):
            return False
    return True

def count_circular_primes(limit):
    count = 0
    for n in range(2, limit):
        if is_circular_prime(n):
            count += 1
    return count

# Example usage
limit = 100
print(count_circular_primes(limit))  
