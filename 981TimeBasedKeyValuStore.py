class TimeMap(object):
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.store:
            return ""

        array = self.store[key]

        last, l, r = None, 0, len(array) - 1

        while l <= r:
            middle = (l + r) // 2
            if array[middle][0] > timestamp:
                r = middle - 1
            elif array[middle][0] < timestamp:
                l = middle + 1
                last = middle
            else:
                return array[middle][1]

        if last is None:
            return ""

        return array[last][1]


timeMap = TimeMap()
timeMap.set("foo", "a", 1)
timeMap.set("foo", "b", 3)
timeMap.set("foo", "c", 6)
timeMap.set("foo", "d", 10)
print(timeMap.get("foo", 4))
