# Quicksort
<!-- Short summary or background information -->
In this repo, we implement radix sort. Radix sort is different from other sorting algorithms. Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value. Notice that we only deal within the natural number domain. (aka. positive intergers including 0)


## Challenge
<!-- Description of the challenge -->
The major challenge here is the mechanism. The way radix compare is very different from all other sorting algorithms we have seen. It pick and compare digits. And the sorting also rely on the 'keep original sequence if having tiers.'


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The solution contains two parts:
1. we iterate through the list to find the longest digit we ever need to go through.
2. for each digit position, we check each value within the list, save them into buckets, give back a merged bucket at the end of each iteration.

The big O time is O(d*n), where d is the longest digit we ever need to go through (e.g. d of 123 for base 10 = 3)
The big O space is O(n), since each step we create a new tmp storage to store the new order.


## Solution
<!-- Embedded whiteboard image -->
