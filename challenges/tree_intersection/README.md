# Intersection of binary trees
<!-- Short summary or background information -->
In this file, we write a function called tree_intersection that takes two binary tree parameters. Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Challenge
<!-- Description of the challenge -->
The main challenge is how to do pass along information while traversing. I tried to add a 'methodToRun' argument to preOrder I defined for binary search tree class, but didn't figure out how to grab local value and pass it into a newly defined methodToRun...maybe set a dummy for value attribute for the def?...hum...

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The time complexity will be O(n) as we only traverse each node once.
The space complexity will be O(n) in the worst case as we need to store node from tree1 into the dictionary.


## Solution
<!-- Embedded whiteboard image -->
