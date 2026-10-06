from collections import defaultdict

# Defaultdict even if the key is not there , it automatically create a list for that key defaultdict(list)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # nlogn * m  not usually optimal 
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())




        