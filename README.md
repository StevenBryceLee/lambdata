# lambdata
Python Package with Data Science Utilities

The point of this class is to write different functions for high quality OOP principles

This includes initializing the file, setup requirements, class examples, 
with the capability of importing this class from pypi.org

While this package can be imported and used, it does not have a coherent function or purpose

oop_examples.py contains a class which solves this hackerrank challenge:
https://www.hackerrank.com/challenges/maze-escape?hr_b=1

This has a simulator for a board, along with a 'next_move' function which is what is actually required 
to solve the puzzle

The bot can only see its immediate surroundings, and is oriented randomly at the start of the game
The bot will check to see if it can see the exit, then check to see if it can follow a wall, then it will move 
in order of up, left, down, right depending on what is possible.

