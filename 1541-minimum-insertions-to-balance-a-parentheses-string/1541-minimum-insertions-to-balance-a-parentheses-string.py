
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open_needed += 2

                # If open_needed is odd, insert one ')'
                if open_needed % 2 == 1:
                    insertions += 1
                    open_needed -= 1

            else:
                open_needed -= 1

                # No opening parenthesis available
                if open_needed < 0:
                    insertions += 1
                    open_needed = 1

            i += 1

        return insertions + open_needed