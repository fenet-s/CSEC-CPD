class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result += 1
        str(result)
        list_of_digits = [int(digit) for digit in str(result)]

        return list_of_digits