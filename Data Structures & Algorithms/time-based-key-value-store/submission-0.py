class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = (value, timestamp)
        self.map.setdefault(key,[]).append(val)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.map:
            values = self.map.get(key)
            l, r = 0, len(values)-1
            while l <= r:
                mid = (l+r)//2
                if timestamp >= values[mid][1]:
                    res = values[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
        return res
