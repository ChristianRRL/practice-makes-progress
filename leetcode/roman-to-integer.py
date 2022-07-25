class Solution(object):
    # IF there was an __init__
    # THEN I might pass in variables like...
    # self.nums = var1
    # selv.target = var2
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        _dict = {"I":1
                ,"V":5
                ,"X":10
                ,"L":50
                ,"C":100
                ,"D":500
                ,"M":1000
            }
        
        _sum = 0
        prev = 0
        # for c in s:
        for c in reversed(s):
            if _dict[c] == prev:
                _sum += _dict[c]
            elif _dict[c] >= prev:
                _sum += _dict[c]
            else:
                _sum -= _dict[c]
            prev = _dict[c]
                
        
        # MAYBE think about roman numerals as "SUMMING" in reverse order
        # e.g. "MCMXCIV"
        # Start with the last character V > 5
        # Then word my way to the left..
        # IF the next character is SMALLER than my current character, SUBTRACT
        # IF the next character is GREATER THAN OR EQUAL TO then SUM
        
        return _sum

# s = 'III'
# obj = Solution()
# print(obj.romanToInt(s))