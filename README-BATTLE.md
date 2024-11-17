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

The image below shows what happens if the player runs out of turns. A message is displayed to notify them and the ship is finally displayed on the grid with an S and the co-ordinates are also provided.
![BS - End of game](https://github.com/user-attachments/assets/1fac3e97-2be8-4d4c-8eb5-93d793287987)




