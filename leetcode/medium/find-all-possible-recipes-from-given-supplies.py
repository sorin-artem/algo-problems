from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {}
        for s in supplies:
            can_cook[s] = True
        recipe_index = {}
        for i, r in enumerate(recipes):
            recipe_index[r] = i

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False

            can_cook[r] = False
            for neighbor in ingredients[recipe_index[r]]:
                if not dfs(neighbor):
                    return False
            can_cook[r] = True
            return can_cook[r]

        res = []
        for r in recipes:
            if dfs(r):
                res.append(r)

        return res