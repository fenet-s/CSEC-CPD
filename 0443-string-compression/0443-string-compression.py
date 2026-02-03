class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        result = []
        
        for r in range(1, len(chars) + 1):
            if r < len(chars) and chars[r] == chars[l]:
                continue
            else:
                count = r - l
                result.append(chars[l])
                if count > 1:
                    result.extend(list(str(count)))
                l = r
        
        chars[:] = result
        return len(result)
