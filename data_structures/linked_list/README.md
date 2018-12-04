# linked list implementation

**Author**: Toby  
**Version**: 1.0.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
In this repository, I implement a singly linked list based on a standard node class.

## Challenge
<!-- Description of the challenge -->
12/3/18:  
The class has an .append(value) function which adds a new node with the given value to the end of the list  
The class has an .insertBefore(value, newVal) function which adds a new node with the given newValue immediately before the first value node  
The class has an .insertAfter(value, newVal) function which adds a new node with the given newValue immediately after the first value node  
The class has a .delete_node(value) function which removes the first node with the given value from the linkedlist.  

11/30/18:  
The linked list class will have default value equlas to None for head when the list is created.
The linked list class has a len function to represent how many nodes in the list.
The linked list can take iterable as an argument and turn that iterable object into a linked list.
e.g. linked_list([1,2,3,4]) = a linked list with nodes (head)4, 3, 2, 1
The linked list also has insert(element) function to add element into the linked list, and a includes(element) function that tells you whether the element exists in the linked list.


## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
To run the linked_list.py code on your machine, you will need python 3.6.
To run the test_linked_list.py via pytest, you will need both python 3.6 and pytest.


## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
Singly linked list is a python class build based on Node class. It's essentially a list of nodes that are connected by using class method "._next". Users can put any data into the nodes and thus linked list.

## Solution
<!-- Embedded whiteboard image -->
![linked_list_insertion_whiteboard](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/LL_insert_whiteboard.jpeg)

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available yet.


## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:-->

11/30/18: 2pm, first edition on.  
12/3/18: 3pm, added Linked List Insertions.

