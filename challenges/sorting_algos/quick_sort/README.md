# Quicksort
<!-- Short summary or background information -->
In this file, we implement the classic quick sort with middle point for pivot value.

e.g. for a in_list [3,5,11,2,-1,10],
if we want to sort the whole part: quick_sort(in_list, 0, 5)
if we only want to sort the later half: quick_sort(in_list, 3, 5)

## Challenge
<!-- Description of the challenge -->
The main challenges of quick sort are:
1. swap in place.
2. recrusive call.
3. partition.
4. select middle point as starting pivot instead of the leftmost point.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The main advantage of quicksort is its low time complexity by keep partitioning input list into three parts (pivot point, left to pivot point, and right to pivot point). Each time we arrange the list as all the values smaller than pivot point will be to the left, and all the values larger or equal to pivot point will be to the right. To make it more efficient, I switch the starting pivot to be the middle point (not medium but the one in the middle position) each time to prevent the leftmost-worst-case issue (can be found in the reference link).
As a result, our time complexity can be O(nlogn) on average.
And since we modify the input list inplace, our space complexity will be close to O(1) at most of the time, but can get to O(n) if unlucky.

## Solution
<!-- Embedded whiteboard image -->


## Referemce
http://me.dt.in.th/page/Quicksort/
