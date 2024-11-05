import random


class RandomizedSet:

    def __repr__(self):
        return str(self.nums_map) + str(self.nums_list)

    def __init__(self):
        self.nums_map = {}
        self.nums_list = []

    def insert(self, val: int) -> bool:
        if val in self.nums_map:
            return False
        self.nums_map[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.nums_map:
            index = self.nums_map[val]
            last_value = self.nums_list[-1]
            self.nums_list[index] = last_value
            self.nums_list.pop()
            self.nums_map[last_value] = index
            del self.nums_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums_list)


obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(4)
param_2 = obj.remove(1)
print(obj)
param_3 = obj.getRandom()
