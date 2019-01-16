# Intersection of binary trees
<!-- Short summary or background information -->
In this file, we write a function called tree_intersection that takes two binary tree parameters. Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Challenge
<!-- Description of the challenge -->
The main challenge is how to do pass along information while traversing. I tried to add a 'methodToRun' argument to preOrder I defined for binary search tree class, but didn't figure out how to grab local value and pass it into a newly defined methodToRun...maybe set a dummy for value attribute for the def?...hum...

Another challenge is to make duplicate look up more efficient.
The most simple way will be to have a list and use 'in' method. But this is O(n) time complex. A better way is to use hash table to look up. I didn't find much info about time difference between using 'a in dict.keys()' and 'a in dict.values()', but I'm assumming the first one uses hash and second one has to go into value lists. I used a timeit and find the first one is slightly faster than the second (with len(lists) in dict.values() be about 10).

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The time complexity will be O(n) as we only traverse each node once.
The space complexity will be O(n) in the worst case as we need to store node from tree1 into the dictionary.


## Solution
<!-- Embedded whiteboard image -->
