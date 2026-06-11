from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq= defaultdict(list)
        for word in strs:
            count= [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            freq[tuple(count)].append(word)
        return list(freq.values())