from typing import List

# brute force O(n^2)
# def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # i = 0
    # while i < len(gas):
    #     tank = gas[i]
    #
    #     steps_amount = 0
    #     current_station = i
    #     next_station = i
    #     while steps_amount < len(gas):
    #         next_station += 1
    #         if next_station == len(gas):
    #             next_station = 0
    #         if tank >= cost[current_station]:
    #             tank -= cost[current_station]
    #             tank += gas[next_station]
    #             steps_amount += 1
    #         else:
    #             break
    #         current_station = next_station
    #
    #
    #     if steps_amount == len(gas):
    #         return i
    #     i += 1
    #
    # return -1
def array_sum(list):
    res = 0
    for element in list:
        res += element
    return res
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    start = 0
    for i in range(len(gas)):
        total += gas[i]
        total -= cost[i]
        if total < 0:
            total = 0
            start = i + 1
    return start



print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))