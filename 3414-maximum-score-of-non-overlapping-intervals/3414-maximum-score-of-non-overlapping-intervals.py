class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Store original index
        arr = []

        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by start time
        arr.sort()

        n = len(arr)

        # Starts of intervals
        starts = [x[0] for x in arr]

        dp = {}

        def fun(ind, limit):

            if ind >= n or limit == 4:
                return 0, []

            state = (ind, limit)

            if state in dp:
                return dp[state]

            # ----------------
            # NOT TAKE
            # ----------------
            not_score, not_indices = fun(ind + 1, limit)

            # ----------------
            # TAKE
            # ----------------
            l, r, w, original_index = arr[ind]

            # Need next_start > r
            next_ind = bisect_right(starts, r)

            take_score, take_indices = fun(next_ind, limit + 1)

            take_score += w
            take_indices = [original_index] + take_indices

            # ----------------
            # Compare
            # ----------------
            if take_score > not_score:
                dp[state] = (take_score, take_indices)

            elif not_score > take_score:
                dp[state] = (not_score, not_indices)

            else:
                # Same score
                take_sorted = sorted(take_indices)
                not_sorted = sorted(not_indices)

                if take_sorted < not_sorted:
                    dp[state] = (take_score, take_sorted)
                else:
                    dp[state] = (not_score, not_sorted)

            return dp[state]

        score, indices = fun(0, 0)

        return sorted(indices)