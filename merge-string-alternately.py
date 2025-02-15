class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        merged_string = ""
        l, r = 0, 0

        # The while loop will stop when the end of the shortest string is reached
        # when l = n1 or r = n2
        while l < n1 and r < n2:
            merged_string += word1[l]
            merged_string += word2[r]
            l += 1
            r += 1

        # Adding the characters that weren't added due to the shorter string
        # As stated earlier, when reaching the end of the string, l = n1 or
        # r = n2, so 1 while loop will be skipped at least
        while l < n1:
            merged_string += word1[l]
            l += 1
        while r < n2:
            merged_string += word2[r]
            r += 1
        return merged_string
