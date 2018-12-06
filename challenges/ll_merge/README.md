# Merge two Linked Lists
<!-- Short summary or background information -->
In this project, we write a function called **mergeLists** which takes two linked lists as input arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped linked list.

## Challenge
<!-- Description of the challenge -->
Try and keep additional space down to O(1).
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I tackled this problem by creating a new linked list object, and wired nodes
from each two input linked list one by one. If one of the linked list ends first,
add the remaining node to our new linked list.

The Big O:
Big O for space shall be O(1) as we are just re-wiring nodes.
Big O for time shall be O(min(a, b)) where a is the length of the first linked
list input, and b be the length of the second linked list input.

## Solution
<!-- Embedded whiteboard image -->
![whiteboard_ll_merge](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/ll_merge_photo.jpeg)
