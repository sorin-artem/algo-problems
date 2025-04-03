class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append((timestamp, value))
        else:
            self.hash_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        timestamps = self.hash_map[key]
        res = ""
        l = 0
        r = len(timestamps) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= timestamps[m][0]:
                res = timestamps[m][1]
                l = m + 1
            else:
                r = m - 1
        print(res)
        return res


def test_time_map():
    timeMap = TimeMap()
    timeMap.set("check", "one", 5)
    timeMap.set("check", "two", 10)
    assert timeMap.get("check", 7) == "one"
    assert timeMap.get("nonexistent", 7) == ""

test_time_map()

