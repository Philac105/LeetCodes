from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs = []
        in_group = set()

        for i in range(len(strs)):
            for j in range(i, len(strs)):
                i_sorted = sorted(strs[i])
                j_sorted = sorted(strs[j])
                if i_sorted != j_sorted or i == j:
                    continue

                new_group = []
                if i not in in_group:
                    new_group.append(strs[i])
                    in_group.add(i)
                if j not in in_group:
                    new_group.append(strs[j])
                    in_group.add(j)

                if len(new_group) == 1:
                    for group in grouped_strs:
                        if strs[i] in group:
                            group.append(strs[j])
                            new_group.remove(strs[j])
                        elif strs[j] in group:
                            group.append(strs[i])
                            new_group.remove(strs[i])

                if new_group:
                    grouped_strs.append(new_group)

        for i in range(len(strs)):
            if i not in in_group:
                grouped_strs.append([strs[i]])

        return grouped_strs