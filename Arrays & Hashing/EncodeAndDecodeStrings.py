from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += f"{len(str)}#{str}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = j + length + 1
            word = s[start:end]
            decoded_str.append(word)
            i = end

        return decoded_str
