class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_sum = skill[0] + skill[-1]
        total_product = 0
        left, right = 0, len(skill) - 1
        
        while left < right:
            current_sum = skill[left] + skill[right]
            if current_sum != total_sum:
                return -1
            total_product += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return total_product
