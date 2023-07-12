
import math
class Solution(object):
    # def countPrimes(self, n):
    #     count = 0

    #     for i in range(2, n):
    #         is_prime = True

    #         for j in range(2, int(math.sqrt(i)) + 1):
    #             if i % j == 0:
    #                 is_prime = False

    #         if(is_prime):
    #             count += 1
    #             print(i)

    #     return count
    # def countPrimes(self, n):
    #     seen = [False] * n
    #     number_of_primes = 0
    #     for i in range(2, n):
    #         # If the number is already in the map as true, go to the next iteration
    #         if(seen[i] == True):
    #             continue
    #         # If its not in the map, then its a prime, get all the multiples up to n to the map
    #         number_of_primes += 1
    #         for j in range(i, n, i):
    #             seen[j] = True
        
    #     return number_of_primes
    # def countPrimes(self, n):
    #     if n < 2: return 0
    #     primes = [1] * n
    #     primes[0] = primes[1] = 0

    #     for i in range(2, n):
    #         if(primes[i]):
    #             primes[i*i:n:i] = [0] * len(primes[i * i: n: i])
    #     return sum(primes)

    # 99% solution
    def countPrimes(self, n):
        if n < 2: return 0
        primes = [1] * n
        primes[0] = primes[1] = 0

        for i in range(2, int(math.sqrt(n))+1):
            if(primes[i]):
                primes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
        return sum(primes)

answer = Solution()
print(answer.countPrimes(100))