# Hashmap LEFT JOIN
<!-- Short summary or background information -->
In this file, we write a function that left joins two hashmaps into a single data structure (list). All value in hashmaps are strings.


## Challenge
<!-- Description of the challenge -->
The challenge is about matching. If we match word pairs iterately, it could take upto O(a * b) time to complete matching. (a = len(input1), b = len(input2))


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
We take advantage of O(1) look up in hashmap to make this left join taking only O(a) time.
The space complexity is O(a) as we need to store all inputs in hashmap1 into a new data structure.

## Solution
<!-- Embedded whiteboard image -->
![whiteboardsolution](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/left_join_whiteboard.jpeg)
