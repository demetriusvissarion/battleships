Battleships Project
This is a project aimed to develop all of your skills so far. It is designed to be challenging for most learners on the Makers immersive course.

Your assignment is to design and test-drive a terminal-based Battleships game. A small amount of code is already written, to get you started and show you the approach to building and testing terminal user-interfaces using mocking.

Getting Started
How to get started:

; pipenv install # To install dependencies

; pipenv run pytest # All tests should pass
; pipenv run pytest --cov lib # To see test coverage too

; pipenv run python run.py
This will give you a few prompts and show you a board.


You might want to start by reading through the existing code. Since this is advanced content, there are a few new techniques included for you to investigate.

After this, pick a few user stories from below, design your classes, and start test-driving. Note that the classes here are not the full set of classes necessary for a good program design. As you build, you will need to break apart classes and add new ones.

# User Stories
Here is the full set of user stories for this game. Some are already implemented.

As a player
So that I can prepare for the game
I would like to place a ship in a board location

As a player
So that I can play a more interesting game
I would like to have a range of ship sizes to choose from

As a player
So the game is more fun to play
I would like a nice command line interface that lets me enter ship positions and
shots using commands.

As a player
So that I can create a layout of ships to outwit my opponent
I would like to be able to choose the directions my ships face in


5. As a player
So that I can have a coherent game
I would like ships to be constrained to be on the board


6. As a player
So that I can have a coherent game
I would like ships to be constrained not to overlap
   => completed but has a bug: overlap ships if intersection > 1st point
        => add 3rd argument 'position' (defaults=None) to game.ship_at & ship_placement.covers
        => add 4th argument 'length' (defaults=None) to game.ship_at & ship_placement.covers
      => fixed bugg
_________________________________________________________________________________

7. As a player
So that I can win the game
I would like to be able to fire at my opponent's board

8. As a player
So that I can refine my strategy
I would like to know when I have sunk an opponent's ship

9. As a player
So that I know when to finish playing
I would like to know when I have won or lost

10. As a player
So that I can consider my next shot
I would like to be able to see my hits and misses so far

11. As a player
So that I can play against a human opponent
I would like to play a two-player game