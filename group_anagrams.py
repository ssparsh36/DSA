class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            dict["".join(sorted(i))]=[]
        for i in strs:
            dict["".join(sorted(i))].append(i)
        return(list(dict.values()))
        
