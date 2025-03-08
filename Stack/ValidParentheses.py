
char_set = {
    '(': ')',
    '{': '}',
    '[': ']',
}

class Solution:
    def isValid(self, s: str) -> bool:
        opening_char = []

        for c in list(s):
            if c in char_set:
                opening_char.append(c)
            else:
                if len(opening_char) < 1:
                    return False
                last_char = opening_char.pop()
                if c == char_set[last_char]:
                    continue
                return False

        if len(opening_char) < 1:
            return True
        return False
