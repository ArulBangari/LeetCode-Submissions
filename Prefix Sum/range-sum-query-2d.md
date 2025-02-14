# [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/description/)
## Explanation
To be able to follow the **SumRegion** working on **0(1)** time complexity, you have to use a 2D prefix sum array. A 2D prefix sum array stores, for each element, the sum of all elements preceding it in row and column order.
Create the 2D prefix array.Then use the 2D prefix array to find the sum of the elements of the matrix inside the rectangle. To do this, follow the following steps:
* Find the sum of the elements at the lower right corner **(row2, col2)**, which will give the sum of elements from **(0,0)** to **(row2, col2)**.
* Subtract the sum of elements at the upper right corner **(row1 - 1, col2)**. Using **row1** will include the 1st row (which we want in the sumRegion rectangle) in the subtraction. This will leave the sum of the elements from **(row1, 0)** to **(row2, col2)**.
* Subtract the sum of elements at the lower left corner **(row2, col1 - 1)**. As stated earlier, using **col1 - 1** makes it so that **col1** will not be subtracted as well. This will leave the sum of the elements from **(row1, col1)** to **(row2, col2)** but will subtract an extra area sum of **(0,0)** to **(row1 - 1, col1 -1)**.
* Add the area sum that was subtracted twice, to get the sum of the elements in the rectangle.

## Code Explanation
### def __init__(self, matrix: List[List[int]]):
In this method, I am initializing the sum prefix array. To make it easier and to account for edge cases, it is best to make all the elements in the 0 column and row 0. Pretty much, the 2D prefix sum array is not "0-indexed" like the matrix is. This means that the prefix sum at **[row, column]** is for the **matrix[row - 1, column - 1]**.
The element of each cell in the 2D array is equal to the matrix element plus the prefix sum at the cell to the left of it plus the prefix sum at the cell above it minus the double counted area. As stated earlier, when I am looping through the array, I am one behind in terms of column and row.

### def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
This is doing what was explained in the [Explanation section](#explanation), but I did convert the row and column indices to match the 2D prefix array.
