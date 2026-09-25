class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def build(s):
            parts = set()
            curr = {""}
            i = 0

            while i < len(s):

                if s[i] == '{':
                    j = i + 1
                    depth = 1

                    while depth:
                        if s[j] == '{':
                            depth += 1
                        elif s[j] == '}':
                            depth -= 1
                        j += 1

                    options = build(s[i + 1:j - 1])

                    curr = {
                        a + b
                        for a in curr
                        for b in options
                    }

                    i = j

                elif s[i] == ',':
                    parts |= curr
                    curr = {""}
                    i += 1

                else:
                    curr = {
                        x + s[i]
                        for x in curr
                    }
                    i += 1

            parts |= curr
            return parts

        return sorted(build(expression))
