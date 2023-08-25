class Solution(object):
    def carFleet(self, target, position, speed):
        cars = [[p, s] for p, s in zip(position, speed)]

        cars.sort(key=lambda x: x[0], reverse=True)

        slowest, ans = float("-inf"), 0

        for car in cars:
            time = (target - car[0]) / car[1]
            if time > slowest:
                slowest = time
                ans += 1

        return ans


answer = Solution()
print(answer.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(answer.carFleet(11, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(answer.carFleet(100, [0, 2, 4], [4, 2, 1]))
print(answer.carFleet(10, [6, 8], [3, 2]))
