class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        res = set()

        def is_valid(path):
            balance = 0

            for c in path:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        def fun(ind, path):
            if ind == n:
                if is_valid(path):
                    res.add(path)
                return
            c = s[ind]
            fun(ind + 1, path + c)

            # Remove current character only if it is a parenthesis
            if c == '(' or c == ')':
                fun(ind + 1, path)

        fun(0, "")

        # Find maximum length valid strings
        max_len = 0

        for string in res:
            max_len = max(max_len, len(string))

        return [string for string in res if len(string) == max_len]