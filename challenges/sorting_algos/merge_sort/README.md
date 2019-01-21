# Mergesort
<!-- Short summary or background information -->
In this repository we implement the classic merge sort via top-down fashion.


## Challenge
<!-- Description of the challenge -->
The usually challenge of merge sort is to correctly structure the recursive loop.
For top-down fashion, we first split the input list into left and right, call merge_sort recursively on left and right. At the end of the function, we call a helper function to merge sorted left and right back into a sorted input list.
This approach takes advantage of the fact that list with length == 1 is already sorted.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O time is O(nlogn), as the spliting process takes O(logn) time and each time we split, we need to merge it back later. And merging takes O(n) time as it needs to iterate through every element.
Big O space is O(1), as we only create pointers and one additional data structure (a list), and we only add element into this new list by using pop(). Thus the total memory usage shall be constant.


## Solution
<!-- Embedded whiteboard image -->
