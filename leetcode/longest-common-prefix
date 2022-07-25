class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type s: List[str]
        :rtype: str
        """
        
        # Think.. how do I take any list of strings and find the common "prefix"
        # I could index all characters from the first provided string
        # and then "attempt" to match it to subsequent strings
        # 
        
        # init pref string to keep track of the prefix
        pref = strs[0]
        
        # prefix index tracker
        index = len(pref)
        
        for s in strs:
            print(s)
            while(pref[:index] != s[:index]):
                index -= 1
        
        print(pref,index)
        return pref[:index]
