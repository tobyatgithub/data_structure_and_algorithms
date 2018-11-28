# array-shift


**Author**: Toby!  
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->

In this file, we create a function that will take a list and the value as inputs, add the value into the middle index of the list 
and return this new list as output.  


## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
in Terminal, go to the directory, and then type in "python snake_cafe.py" to run the code.
To get it run on any local computer, you will need python 3.6, and pytest package.
To run the array_shift.py file, go to the directory, in terminal type: python array_shift.py
To run the test_array_shift.py file, same directory, in terminal type: pytest -v


## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
This array_shift.py is written in python 3.6 with all default functions (no library import required.)
The test_array_shift.py requires python 3.6 with pytest package.

## Challenge
<!-- Description of the challenge -->
The main challenges here are:
1. insert the value into the later half if given an odd length list
2. the actual insert process in python
3. exception handling.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
1. for the first challenge, I used (len(inArray)+1)//2 to ensure it always insert into the middle or later half
2. I used python slice to do the actual insertion
3. used try-exception for error handling.

The Big O time will be O(n), as we will need to get to the middle point and paste everything. 
And Big O space shall be O(1), as we don't create any new varaiable to store or handle data.


## Solution
<!-- Embedded whiteboard image -->
![White_Board](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/array_shift/assets/array_shift.jpg)


## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available right now.

## Change Log
11/27/18 edition 1
