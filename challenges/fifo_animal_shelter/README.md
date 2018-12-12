# First-in, First out Animal Shelter.
<!-- Short summary or background information -->
In this projct, I created a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.

## Challenge
<!-- Description of the challenge -->
The main challenge here is to use node-like objects to create a class similar to priority queue. (on GeekforGeeks they used list to implement which is way too easy hahaha.)
With node-like objects, properly managing self.front and self.back becomes a real challenge.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The two main methods are enqueue() with object, and dequeue() with preference.
For enqueue, big O space = O(1), and big O time = O(1), since we always add at the end (self.back)
For dequeue, big O space = O(1), ad big O time varies. The worst case for big O time is O(n) where we need to traverse through the whole queue to find the object to drop/pop.

## Solution
<!-- Embedded whiteboard image -->
![code_challenge12_whiteboard](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/code_challenge12.jpg)
