# data_structure_and_algorithms

**Author**: Toby!
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->

This is the root repository for all the data structure and algorithm challenge realated content. All structure and challenge require implement without utilizing any of the built-in methods available. Any functionality that you write shall be tested.

Contents:
1. [Array Shift](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/challenges/array_shift):  
Write a function that takes in an array and the value to be added. Return an array with the new value added at the middle index.

2. Binary Search:  
Write a function that takes in 2 paramters: a sorted array and the search key. Return the index of the array's element that is equal to the search key, or -1 if the element does not exist.

3. [Data Structure] [Linked List](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/data_structures/linked_list):  
* Create a class for a **Node** which is aware of the value as "val" and next as "_next".
* Create a class for **LinkedList** which creates an empty Linked List with None assigned to head when instantiated.
* The LinkedList class shall be aware of the length of the linked list.
* This class should have the ability to accept an iterable as an argument when instantiated (such as [1,2,3,4]) and creates a new Node in the list for each value in the iterable.
* Define your customized print magic function.
* Define a method called **includes** that returns boolean depending on whether a value exists as a Node value within the list.
* Catch and handle any exceptions and return a printed value or operation to cleanly represents the state and provides the user with clear direction and output.
* Write .append(value) for your linked list class such that adds a new node with the given value to the end of the list.
* Write .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first node whose val == value input.
* Write .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first node whose val == value input.

4. [linked list kth from end](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/data_structures/linked_list):  
Write a method of Linked List class which takes in a number k. Return the node's value that is k from the end of the linked list. Return None if impossible.

5. [linked list merge](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/challenges/ll_merge):  
Write a function that takes in two linked list as arguments, zip the two linked lists into one such that the nodes alternate between the two lists and return a reference to the head of the zipped list. Keep space complexity to O(1).

6. [Data Structure] [Stack](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/data_structures/stack) and [Queue](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/data_structures/queue):
* Use the Node class from previous, create a class for **stack** which shall be aware of a default None value assigned to top when instantiated.
* This **stack** class shall be aware of the length of the stack.
* This **stack** class shall be able to take in iterables as argument when instantiated.
* Define magic methods such as str and repr to support user functionality.
* Define a method called **push** which takes any value as an argument and adds to the top of the stack with O(1) time complexity.
* Define a method called **pop** which takes no argument and returns the Node at the top of the stack.

* Use the Node class from previous, create a class for **queue** which shall be aware of a default None value assigned to front and back when instantiated.
* This **queue** class shall be aware of the length of the queue.
* This **queue** class shall be able to take in iterables as argument when instantiated.
* Define magic methods such as str and repr to support user functionality.
* Define a method called **enqueue** which takes any value as an argument and adds that value to the back of the queue with O(1) time complexity.
* Define a method called **dequeue** which takes no argument, removes and returns the Node at the front of the queue.

7. [queue with stacks](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/challenges/queue_with_stacks):  
Write a function that only uses stack to realize functionality of a queue. You shall only use no more than "push", "pop", and "peek" methods in your stack class.

8. [fifo animal shelter](https://github.com/tobyatgithub/data_structure_and_algorithms/tree/master/challenges/fifo_animal_shelter):
* Create a class called **AnimalShelter** which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
* Implement an **enqueue(animal)** method that adds animal to the shelter. Animal can be either a dog or a cat object.
* Implement an **dequeue(pref)** method that returns either a dog or a cat. Return None if no pref specified. (Stretch: if no pref specified, return whichever animal that has been waiting in the shelter for the longest time.)

9. multi bracket validation


## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
in Terminal, go to the directory, and then type in to run the code in python.


## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
This main code is written in python 3.6 with all default functions (no library import required.)
The test code is realized by using pytest



## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available right now.

## Change Log
11/27/18-created and added array_shift()

