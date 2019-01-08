# Find Edges
<!-- Short summary or background information -->
In this repository I wrote a function that takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.

## Challenge
<!-- Description of the challenge -->
The main challenge here is iterate through multiple cities from the given list.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach is straightforwad, I use a for loop to iterate through the list, each iteration I grab the from_city and to_city, see whether they are connected and the cost between if they are connected. If one trip among many is impossible, I break the loop immediately and return (False,0). The Time efficiency shall around O(n), as we will not visit the input list more than once, (but could end earlier if one trip in the middle is impossible.) The Space efficiency shall be O(1), as the algorithm doesn't require any additional data storage.

## Solution
<!-- Embedded whiteboard image -->
![white board picture](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/get_edge_whiteboard.jpeg)
