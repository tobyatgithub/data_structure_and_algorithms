# Binary Search

**Author**: Toby  
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
<!-- Short summary or background information -->
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. We used binary search in the guessing game in the introductory tutorial.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
To run the array_binary_search.py code on your machine, you will need python 3.6.  
To run the test_array_binary_search.py via pytest, you will need both python 3.6 and pytest.  


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


## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available yet.


## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:-->
11/28/18: First edition. Talked with Shannon on having the mid_index * (___ != -1). It's a good idea compared to having if conditions trying to check boundary situations. For exmaple:  
```python
if array[first_half][-1] < value: 
    return -1
``` 

