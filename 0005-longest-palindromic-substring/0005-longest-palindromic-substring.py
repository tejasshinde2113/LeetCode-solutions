class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform the string to handle both odd and even length palindromes uniformly
        T = '#'.join('^{}$'.format(s))  
        n = len(T)
        P = [0] * n
        C = R = 0  # Center and right boundary
        max_len = 0
        center_idx = 0

        for i in range(1, n - 1):
            mirror = 2 * C - i  # Mirror index of i around center C
            
            if i < R:
                P[i] = min(R - i, P[mirror])  # Use previously computed values
            
            # Expand around center i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # Update center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]
            
            # Track the longest palindrome found
            if P[i] > max_len:
                max_len = P[i]
                center_idx = i

        # Extract longest palindromic substring from the original string
        start = (center_idx - max_len) // 2  # Convert back to original indices
        return s[start: start + max_len]
