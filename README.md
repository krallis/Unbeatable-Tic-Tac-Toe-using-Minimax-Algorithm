# Unbeatable-Tic-Tac-Toe-using-Minimax-Algorithm

This is an implementation of the Tic-tac-toe game. A user plays against pc (AI). The AI is unbeatable, because it uses minimax for playing its moves.

## What is a Minimax algorithm ?
A minimax algorithm is very common in game theory and can be applied in cases where players compete with each other. Such cases are the tic-tac-toe game which is presented here, as well as other games that involve decision making, like Backgammon and Chess.

A minimax algorithm tries to make the decision which is more likely to win the game. For doing so, it scans all the possible combinations of moves for both players and chooses the one that leads to a not-losing terminal state. For doing so, it needs a way to evaluate if a move is better than another one. It simulates the moves of two different antagonist players which are considered to play optimaly. Because it scans all possible combinations, for complicated games like chess, it can become computationaly heavy.

## Tic-tac-toe Implementation
The case of tic-tac-toe can be considered somehow restricted, because the board is only 3x3 and the number of players is 2. In this implementation the move of User is represented by -1 and the move of AI is represented by 1. An empty position in the board is represented by 0. Thus we can use those values to check if someone has won, or if the game is still on. The board evaluation function returns -10 if Player has won and 10 if AI has won. In any other case, board evaluation function returns 0. Those are also the values used to determine wheather a move is good or bad for the player.

In the minimaxAlg function the two antagonist players can be seen. There is a maximizer and a minimizer player. Tha maximizer player tries to play optimaly meaning that tries to find the move with the maximum evaluation score. The minimizer player tries to find the move with the minimum evaluation score. For the AI the best move coincides with the best move of the maximizer player. Thus we select the best move to be the one with the maximum value (with bestValue() function).

Player gives his/hers desired move through the console. The board can be also previewed in the console.

