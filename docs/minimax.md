# Minimax AI

## 1. Overview

The computer opponent uses the **Minimax algorithm** to evaluate possible moves and choose the action with the highest estimated value.

Minimax is a decision-making algorithm commonly used in two-player, turn-based games. It assumes that both players make decisions optimally:

- The maximizing player tries to obtain the highest possible score.
- The minimizing player tries to obtain the lowest possible score for the maximizing player.

In this project, the computer is the maximizing player, while the human opponent is the minimizing player.

The implementation is located in `start_game/minmax.py`, in the `MinimaxAI` class.

## 2. Search Depth

The AI uses a depth-limited search with a default maximum depth of 4.

This means that it explores a sequence of possible moves up to four search levels deep before evaluating the resulting board position.

The search depth is configurable through the `max_depth` constructor parameter.

```python
MinimaxAI(board, symbol, opponent_symbol, max_depth=4)
```

A greater search depth allows the algorithm to consider more future possibilities, but also increases the number of positions it must evaluate.

## 3. Move Generation

The `generate_all_moves()` method generates the possible actions for a player, depending on the current phase.

### Placement Phase

During Phase 1, every empty board position is a possible move.

Moves are represented as one-element tuples:

```python
(position,)
```

### Movement Phase

During Phase 2, a player can move a piece to an adjacent empty position.

Moves are represented as:

```python
(from_position, to_position)
```

### Flying Phase

During Phase 3, a player with exactly three pieces can move to any empty board position.

The method uses the `can_fly` parameter to determine whether to consider only adjacent positions or all empty positions.

## 4. Board Evaluation

The `evaluate_board()` method assigns a numerical score to the current board state.

A positive score indicates an advantage for the AI, while a negative score indicates an advantage for the opponent.

The evaluation considers several factors.

| Evaluation factor | Weight |
|---|---:|
| Difference in piece count | 100 per piece |
| Difference in mobility | 10 per available move |
| Completed mill | +50 / -50 |
| Potential mill | +15 / -20 |
| Terminal-like conditions | ±9,000 or ±10,000 |

### Piece Count

The difference between the AI's and opponent's piece counts is multiplied by 100.

Having more pieces is generally advantageous because it provides more opportunities for movement and mill formation.

### Mobility

Mobility represents the number of available moves for a player.

The difference between the AI's and opponent's mobility is multiplied by 10.

This rewards positions in which the AI has more movement options and penalizes positions in which the opponent has greater mobility.

### Completed Mills

A completed mill consists of three pieces belonging to the same player in one of the predefined mill combinations.

The AI receives a positive score for its own completed mills and a negative score for the opponent's completed mills.

### Potential Mills

A potential mill is a combination containing two pieces belonging to one player and one empty position.

The evaluation rewards the AI for its potential mills and penalizes the opponent's potential mills.

### Terminal-Like Conditions

The evaluation assigns large scores when one player has no pieces remaining or has no available moves, provided the relevant piece count is nonzero.

These values are intended to make decisive positions more important than ordinary heuristic differences.

## 5. Minimax Recursion

The `minimax()` method recursively explores possible moves.

Its parameters are:

- `depth` — the remaining search depth.
- `is_maximizing` — indicates whether it is the AI's or opponent's turn.
- `phase` — the current game phase used for move generation.

The algorithm stops when the search depth reaches zero or the AI's game-over condition is detected. At that point, it returns the heuristic evaluation of the board.

### Maximizing Turn

When it is the AI's turn:

1. Generate all possible AI moves.
2. Simulate each move.
3. Recursively evaluate the resulting board as a minimizing turn.
4. Undo the simulated move.
5. Keep the highest score.

### Minimizing Turn

When it is the opponent's turn:

1. Generate all possible opponent moves.
2. Simulate each move.
3. Recursively evaluate the resulting board as a maximizing turn.
4. Undo the simulated move.
5. Keep the lowest score.

The recursion alternates between maximizing and minimizing turns until the search depth is reached.

## 6. Move Simulation and Undo

The AI needs to explore possible moves without permanently changing the actual game state.

The `simulate_move()` method temporarily applies a move to the board.

If the move forms a mill, the method also simulates the removal of an opponent's piece.

The method returns the position of the removed piece, if any.

After evaluating the resulting position, `undo_simulated_move()` restores the board to its previous state:

- For a placement, it removes the newly placed piece.
- For a movement, it moves the piece back to its original position.
- If an opponent's piece was removed during the simulation, it restores that piece.

This allows the algorithm to explore multiple candidate moves using the same board object.

## 7. Selecting the Best Move

The `choose_best_move()` method evaluates all possible moves for the AI.

For each candidate:

1. Simulate the move.
2. Call Minimax to evaluate the resulting position.
3. Undo the simulation.
4. Compare the score with the best score found so far.

The move with the highest score is returned.

The class also provides helper methods for choosing placement moves, movement moves, and a piece to remove after forming a mill.

## 8. Limitations and Possible Improvements

The current implementation is a simplified, depth-limited Minimax player. Its evaluation is heuristic, so the selected move is not guaranteed to be optimal.

Some possible improvements include:

- **Alpha-beta pruning:** Avoid exploring branches that cannot influence the final decision.
- **Improved evaluation:** Consider additional strategic factors, such as blocked pieces and the creation of multiple threats.
- **More accurate phase handling:** Model the transition from placement to movement during the search.
- **Turn handling after a mill:** Model the additional turn granted by the standard rules of Nine Men's Morris.
- **Improved terminal-state handling:** Distinguish between the placement phase and later phases when checking whether a player has fewer than three pieces.

These improvements could make the AI more accurate and reduce unnecessary computation.