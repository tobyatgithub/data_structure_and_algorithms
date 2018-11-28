# Binary Search
<!-- Short summary or background information -->
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. We used binary search in the guessing game in the introductory tutorial.


## Challenge
<!-- Description of the challenge -->
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Approach: I use recurrsion to realize the algorithm.
The big O time shall be log(n) since each time we divide the lenght by factor of 2.
The big O space shall be n as we don't save anything extra, so the space will be equal to
the input.

## Solution
<!-- Embedded whiteboard image -->
