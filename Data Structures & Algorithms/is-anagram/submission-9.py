class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        dict1 = {}
        dict2 = {}
        for word in s :
            if word not in dict1:
                dict1[word] = 1
            else:
                dict1[word]=dict1.get(word) + 1

        for word in t:
            if word not in dict2:
                dict2[word] = 1
            else:
                dict2[word]=dict2.get(word) + 1

        for x in dict1:
            if dict1.get(x) != dict2.get(x):
                return False
        return True
        