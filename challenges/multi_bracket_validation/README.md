# Multi-bracket Validation.
<!-- Short summary or background information -->
 In this project, the program take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets: (), [], and {}


## Challenge
<!-- Description of the challenge -->
* match each bracket types
* ignore all other strings (such as alphabets)
* the sequence of brackets matters

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
To tackle this, I used two stacks to store all the brackets in the input string and ignore everything else. And pop from these two stacks once we iterate through the whole input string characters.
Stack is handy here because it takes care of the sequence-matter challenge---as last open bracket is compared against last close bracket.
To compare, I implemented a look up dictionary and save correct pair of brackets to have same value.

The big O space for this problem is near O(n) as we don't need any extra space; and big O time for this problem is O(n)

## Solution
<!-- Embedded whiteboard image -->
