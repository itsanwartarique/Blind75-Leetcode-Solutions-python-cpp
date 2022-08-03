class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for s in strs:
            temp = s
            #sort s
            sort =''.join(sorted(s))
            result[sort].append(temp)  
        return result.values()
