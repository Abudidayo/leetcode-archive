class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap = {}
        
        if len(s) != len(t):
            return False

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for j in t:
            if j not in hashmap or hashmap[j] == 0:
                return False
            hashmap[j] -= 1
        
        return True

        
        
        
        
        