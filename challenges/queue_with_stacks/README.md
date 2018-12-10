# Implement a Queue using two Stacks.
<!-- Short summary or background information -->
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement the standard queue interface, but will internally only utilize 2 Stack objects.


## Challenge
<!-- Description of the challenge -->
In this class, we want to realize two methods:
1. enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
2. dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

However, we shall only use methods belong to Stack instances (push, pop and peek) to complete these two methods.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The space big O is constant O(1) as we don't really create any new data storage (but just how we store out data.)
The time big O is a bit more tricky. For continuous dequeue, it will be O(1); for continuous enqueue, it will be O(1); for any alternative dequeue and enqueue, it will be O(n) as we need to dump pointers from one stack to the other.



## Solution
<!-- Embedded whiteboard image -->
![queue_with_stacks](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/lab_11_queue_with_stacks.jpg)
