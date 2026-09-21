from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        seen = Counter(t)

        saw = {}

        left = 0
        have = 0
        need = len(seen)

        result = ""
        result_len = float("inf")

        for right in range(len(s)):

            # Add s[right]
            if s[right] in saw:
                saw[s[right]] += 1
            else:
                saw[s[right]] = 1

            # Character just became satisfied
            if s[right] in seen and saw[s[right]] == seen[s[right]]:
                have += 1

            # Window is valid
            while have == need:

                # Save smallest window
                if right - left + 1 < result_len:
                    result = s[left:right+1]
                    result_len = right - left + 1

                # Remove s[left]
                saw[s[left]] -= 1

                # Character became unsatisfied
                if s[left] in seen and saw[s[left]] < seen[s[left]]:
                    have -= 1

                left += 1

        return result