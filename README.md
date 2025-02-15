# [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/description/)
## Explanation
To be able to follow the **SumRegion** working on **0(1)** time complexity, you have to use a 2D prefix sum array. A 2D prefix sum array stores, for each element, the sum of all elements preceding it in row and column order.
Create the 2D prefix array.Then use the 2D prefix array to find the sum of the elements of the matrix inside the rectangle. To do this, follow the following steps:
* Find the sum of the elements at the lower right corner **(row2, col2)**, which will give the sum of elements from **(0,0)** to **(row2, col2)**.
* Subtract the sum of elements at the upper right corner **(row1 - 1, col2)**. Using **row1** will include the 1st row (which we want in the sumRegion rectangle) in the subtraction. This will leave the sum of the elements from **(row1, 0)** to **(row2, col2)**.
* Subtract the sum of elements at the lower left corner **(row2, col1 - 1)**. As stated earlier, using **col1 - 1** makes it so that **col1** will not be subtracted as well. This will leave the sum of the elements from **(row1, col1)** to **(row2, col2)** but will subtract an extra area sum of **(0,0)** to **(row1 - 1, col1 - 1)**.
* Add the area sum that was subtracted twice, to get the sum of the elements in the rectangle.

## Code Explanation
### def __init__(self, matrix: List[List[int]]):
In this method, I am initializing the sum prefix array. To make it easier and to account for edge cases, it is best to make all the elements in the 0 column and row 0. Pretty much, the 2D prefix sum array is not "0-indexed" like the matrix is. This means that the prefix sum at **[row, column]** is for the **matrix[row - 1, column - 1]**.
The element of each cell in the 2D array is equal to the matrix element plus the prefix sum at the cell to the left of it plus the prefix sum at the cell above it minus the double counted area. As stated earlier, when I am looping through the array, I am one behind in terms of column and row.

### def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
This is doing what was explained in the [Explanation section](#explanation), but I did convert the row and column indices to match the 2D prefix array.

# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)
## Explanation
Use two pointers to keep track of which index you are on in each string. Then loop through both, while adding letters in alternating order, until you reach the end of the lowest string. Then loop through the string that was longer and add it to the end of the merged string.

## Code Explanation
### def mergeAlternately(self, word1: str, word2: str) -> str:
Pretty much doing what was explained in the [Explanation section](#explanation-1). I use a while loop to check if I've already hit the end of the shortest string. Since I've already hit the end of the shortest string, I don't have to check which string I hit the end of because the tracking index will already be equal to the length of the shorter string, allowing me to skip over the while loop for the shorter string. This is also used in merge sort, but instead of alternating order, you compare and add the lower or higher one to the array depending on if you want the array in descending or ascending order.

# [2698. Find the Punishment Number of an Integer](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/)
## Explanation
A **punishment number** for a positive integer, **n**, is the sum of the squares of all integers **i** such that:
* **1 <= i <= n**
* The string representation of **i * i** can be split into substrings whose integer values sum up to the original number **i**.
To solve this problem, you'll have to use brute force. Loop through each number **1 <= i <= n** and see if the 2nd condition can be satisfied. To see if the 2nd condition is satisfied, try each substring and see if they add up to **i**. Use recursion for this by looping over each digit. For example if you have 1234, the substrings you're looping over are 1, 12, 123, 1234. Then for 1, you'll add 2, 23, 234. For 12, you'll add 3, 34. Lastly for 123, you'll add 4. 1234 is already completed. Then for 1 + 2, you'll add 3, 34. This keeps going until you find the sum of all partitions.
If any of the partitions sum up to **i**, you should add it to the punishment sum.

## Code Explanation
### def checkPunishment(num_str, goal, index, total_sum):
This method recursively loops through **i * i** converted to a string to create the first substrings/partitions. After creating the partitions, it adds the partition to the temporary sum and calls itself again to add the extra substrings/partitions. You want to check if the temporary sum is equal to the goal only when you have reached the end of the number.
### def punishmentNumber(self, n: int) -> int:
This method loops from **1** to **n** and calls the **checkPunishment** method to see if the current number it is on fulfills the 2nd condition stated earlier. If the 2nd condition is satisfied, it adds **i * i** to the punishment number.

# [18. 4Sum](https://leetcode.com/problems/4sum/)
## Explanation
You want to use a 2 pointer strategy for this problem. First sort the array and since the problem wants a 4 numbers that sum up to the target, use nested loops to loop over the the array. Now that you need 2 more numbers, use the 2 pointer strategy. Since the array is sorted, if the sum is greater than the target, subtract 1 from the right pointer. If the sum is less than the target, add 1 to the left pointer. Even if you find a quadruplet, still keep checking because there might be more than 1.

## Code Explanation
### def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
I'm sorting the array, creating the return array, and creating the index(**i1**) for the outer loop. In the outer while loop, I am setting the 2nd index(**i2**) to **i1 + 1** to follow the constraint that **a, b, c, d** are all distinct for the quadruplet. In the inner loop, I set the left pointer(**l**) to **i2 + 1** for the same reason. The right index(**r**) is set to **len(nums) - 1** for the 2 pointer strategy. In the 3rd while loop, I add 1 to the left pointer until it's the next number because I don't want duplicate quadruplets. This is why I do that for **i2** and **i1**.