class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seenChars = {}
        longest = 0;
        length = 0
        count = 0
        lastReset = -1
        for char in s:
            if char in seenChars:
                if length > longest:
                    longest = length
                if seenChars[char] >= lastReset:
                    length = count - seenChars[char] - 1
                    lastReset = seenChars[char] + 1
                else:
                    length = count - lastReset
                seenChars[char] = count
            seenChars[char] = count
            length += 1
            count += 1
        if length > longest:
                    longest = length
        return longest