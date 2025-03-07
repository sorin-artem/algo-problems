class Solution:
    def findMissingAndRepeatedValues(self, grid):
        checked_set = set()
        repeated = None
        correct_sum = (1 + (len(grid) * len(grid))) * (len(grid) * len(grid)) / 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                element = grid[i][j]
                correct_sum -= element
                if element in checked_set:
                    repeated = element
                else:
                    checked_set.add(element)

        return [repeated,  int(repeated + correct_sum)]

print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))