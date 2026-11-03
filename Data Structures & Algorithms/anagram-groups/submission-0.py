class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for output in strs:
            key = "".join(sorted(output))

            if key in groups:
                groups[key].append(output)
            else:
                groups[key] = [output]

        return list(groups.values())
        
