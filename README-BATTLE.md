
## Battleships
Battleships (also known as Battleship) is a strategy type guessing game for two players. It is played on a grid on which a player's ship(s) are concealed from their opponent. The aim of the game is to correctly guess the co-ordinates for the opponent's hidden ship(s) with a correct guess resulting in a hit and sinking your opponent's ship. This game is player vs computer

## User story 
1) As a user I wanted to be able to create a randomly generated grid for the computer to place their ship - I will know I have done this when there is a ship to find on the grid.

2) As a user I wanted to be able to choose co-ordinates as guesses for my turns - I will know I have done this when there are options to input my column and row choices.

3) As a user I wanted to be able to keep track of my turns and know how many I have used - I will know I have done this when my boards update and show what turn I am on.

4) As a user I wanted to be able to visually see where my guesses are on the computer's board - I will know I have done this when I see my previous guesses marked with an M for miss.

5) As a user I wanted to know if my guesses were repeated, not on the grid, not using integers - I will know I have done this when I see error messages shown and instructions on what to do next.

6) As a user I wanted to know whether I had hit my opponent's ship - I will know I have done this when the computer's grid shows with an X and a successful message to let me know I've guessed correctly.

7) As a user I wanted to know where the computer's randomly generated ship was hidden if I didn't manage to find it within all my allocated guesses - I will know I have done this when the computer displays a message stating I have run out of turns and I displays an updated board with an S to demonstrate where the ship was hidden 

## Features

The image below shows how the game starts with an empty grid for the computer and the ship hidded.  The player gets to choose a column and a row to take their turn
![BS - Start](https://github.com/user-attachments/assets/266b5431-3d0e-48db-bd1e-a2e994080feb)

The image below shows that the previous guess is marked on the board and that the turns have increased by one.
![BS - second guess](https://github.com/user-attachments/assets/1783f6be-b7d2-4d39-9260-e263ff96b88a)

The image below shows that the player has placed a guess they have previously taken and ann error message has been returned
advising them to try again.

![BS - guessed previous guess](https://github.com/user-attachments/assets/257807c1-a0d7-4fe9-84ed-555f2394275b)

The image below shows that guesses which are not integers e.g. letters, or guesses which are off the grid are invalid and to
try another guess. The amount of turns the player has still remains until a valid guess is made.
![BS - invalid guesses](https://github.com/user-attachments/assets/69fa9542-baf2-44f0-8eef-e3fa39bc89eb)

The image below shows the message which is displayed when a valid hit is made and that the ship is marked by an X to show it
was hit.

![BS - correct hit](https://github.com/user-attachments/assets/16256b48-b892-4b4d-8b30-8b50b13e5c65)

The image below shows what happens if the player runs out of turns. A message is displayed to notify them and the ship is
finally displayed on the grid with an S and the co-ordinates are also provided.
![BS - End of game](https://github.com/user-attachments/assets/1fac3e97-2be8-4d4c-8eb5-93d793287987)

## Future Features:
If I had more time I would include some of the following features:
1) More ships on the computer's board
2) Player's board to also be shown with the ships visibly placed at the start of the game
3) Ships with greater size than just one co-ordinate.

## Testing:
During the course of building the game I tested the code as I went. I had a number of issues which arose as I started coding:
1)syntax error when displaying the grid to the player; the grid wouldn't show due to the syntax I had typed. I found this error and corrected it.

2)Guess row and column error; the guesses allowed any input to be placed in as guesses and not just integers between 0 and 4. I found the error in the code and managed to fix this.

3)Code not looping; when an incorrect choice had been made the game didn't loop back to prompt the player to guess another choice, there were no other instructions.  I managed to find the error in the coding to ensure it looped back around and gave the player the choice to input a colum and row choice again.

4)Upon starting the game, all the turns were showing; when starting the game X amount of grids showed for the amount of turns available. I corrected this by ensuring the loop was working more efficiently and by ensuring that the print function printed what I needed to to do.

5) When the player typed in a choice which was not an integer, the wrong error message was being displayed "Already Guessed" message was being shown; I fixed this by finding the error in the coding which had missing continue instructions for the loop.

6) Amount of turns increased even when making an incorrect guess; this was fixed by including false statements to prevent the game from moving on to the next turn until a valid guess was made which therefore made the game more fair for the player.

I also test the code through a Pep8 Checker which noted some issues but upon correcting them and making the changes, these seemed to prevent my code from running accurately and caused syntax errors.
![Pep 8 checker](https://github.com/user-attachments/assets/2ca28310-8538-4a82-9152-82c79fa8618d)

## Deployment






