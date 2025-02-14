### [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)
## Explanation
Use two pointers to keep track of which index you are on in each string. Then loop through both, while adding letters in alternating order, until you reach the end of the lowest string. Then loop through the string that was longer and add it to the end of the merged string.

## Code Explanation
### def mergeAlternately(self, word1: str, word2: str) -> str:
Pretty much doing what was explained in the [Explanation section](#explanation). I use a while loop to check if I've already hit the end of the shortest string. Since I've already hit the end of the shortest string, I don't have to check which string I hit the end of because the tracking index will already be equal to the length of the shorter string, allowing me to skip over the while loop for the shorter string. This is also used in merge sort, but instead of alternating order, you compare and add the lower or higher one to the array depending on if you want the array in descending or ascending order.
