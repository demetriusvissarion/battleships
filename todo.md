Battleships Project

How to get started:
; pipenv install # To install dependencies
; pipenv shell
; pipenv run pytest # All tests should pass
; pipenv run pytest --cov lib # To see test coverage too
; pipenv run python run.py


# User Stories
Here is the full set of user stories for this game. Some are already implemented.

1. As a player
So that I can prepare for the game
I would like to place a ship in a board location

2. As a player
So that I can play a more interesting game
I would like to have a range of ship sizes to choose from

3. As a player
So the game is more fun to play
I would like a nice command line interface that lets me enter ship positions and
shots using commands.

4. As a player
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
   => edge placement results in wrong overlap message on opposite side
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


26/12/2023 To add/fix:
 - fix wrong message "That postion is taken by another ship..."
    => edge placement results in wrong overlap message on opposite side
    => 3 // v // 1 // 10 after 3 // v // 1 // 1, or reverse