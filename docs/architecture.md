# Architecture

## 1. Overview

The project follows a modular, layered structure. Its main components are separated according to their responsibilities:

- **Domain layer:** Represents the game entities and board.
- **Service layer:** Implements the game rules and manages the game state.
- **Interface layer:** Handles user interaction through the console or graphical interface.
- **AI layer:** Implements the computer opponent using Minimax.
- **Exceptions:** Defines custom exceptions for invalid game actions.

Both interfaces use the same game service, keeping the core game logic independent of how the game is displayed or controlled.

## 2. Project Structure

```text
domain/
    board.py
    player.py

service/
    game_service.py

start_game/
    minmax.py
    start.py

gui/
    nine_morris_gui.py

user_interface/
    ui.py

exceptions/
    exception_module.py

tests/
    test_minmax.py
    phase1.py
    phase2.py
    phase3.py
```

## 3. Main Components

### 3.1 Domain Layer

#### `Board`

The `Board` class represents the Nine Men's Morris board.

Its main responsibilities are:

- Storing the state of the 24 board positions.
- Maintaining the adjacency relationships between positions.
- Defining all possible mill combinations.
- Checking whether a position is valid or empty.
- Placing and removing pieces.
- Detecting completed mills.
- Checking whether a piece belongs to a mill.

The board is represented internally as a list of 24 positions. Each position contains a player's symbol or a space character when empty.

The adjacency list determines which positions a player can move to during the regular movement phase.

#### `Player`

The `Player` class represents a participant in the game.

It stores player information, including:

- Name and symbol.
- Number of pieces remaining to be placed.
- Number of pieces currently on the board.

It also provides operations for updating piece counts and checking whether the player can still place pieces or is allowed to fly.

### 3.2 Service Layer

#### `GameService`

`GameService` is responsible for managing the game and enforcing its rules.

It maintains:

- The board.
- The two players.
- The current player.
- The current game phase.
- Whether a mill has been formed.
- The game-over state and winner.

Its main operations include:

- `place_piece(pos)` — validates and places a piece.
- `move_piece(from_pos, to_pos)` — validates and performs a move.
- `remove_opponent_piece(pos)` — removes an opponent's piece after a mill.
- `switch_turn()` — changes the active player.
- `check_game_over()` — checks whether the game has reached a winning condition.
- `has_legal_moves(player)` — checks whether a player can make a valid move.
- `get_game_state()` — provides the current game state to the interface.

The service raises custom exceptions when an action requires additional interaction or is invalid. For example, forming a mill raises `RemovalException`, allowing the interface to request the removal of an opponent's piece.

### 3.3 User Interfaces

The application provides two ways to play.

#### Console Interface — `ConsoleUI`

The console interface allows players to interact with the game through textual input and output.

It displays the board, requests player actions, reports invalid moves, and communicates game events.

#### Graphical Interface — `NineMensMorrisGUI`

The graphical interface is implemented with Pygame.

It provides:

- An 800 × 800 game window.
- A visual representation of the board and pieces.
- Mouse-based interaction.
- Piece selection and movement.
- Game status messages.
- An exit button.

The graphical interface also integrates the AI opponent, allowing a human player to compete against the computer.

Both interfaces delegate game-rule validation and state updates to `GameService`.

### 3.4 AI Layer

#### `MinimaxAI`

The AI implementation is located in `start_game/minmax.py`.

Its responsibilities include:

- Generating possible moves.
- Simulating moves on the board.
- Evaluating board positions.
- Exploring possible future moves using Minimax.
- Selecting the move with the best estimated outcome.
- Choosing an opponent's piece to remove after forming a mill.

The AI works directly with the board representation and is integrated into the graphical and console game flows.

A more detailed explanation is available in [minimax.md](minimax.md).

### 3.5 Exceptions

The project uses custom exceptions to represent invalid game actions and special game events.

Examples include:

- `InvalidPlacementPosition`
- `InvalidMoveException`
- `RemovalException`
- `GameException`

This allows the interfaces to handle errors and special situations without embedding the game rules directly into the presentation layer.

## 4. Game Phases

Nine Men's Morris is implemented through three phases.

### Phase 1 — Placement

Each player starts with nine pieces. Players take turns placing their pieces on empty board positions.

When a player forms a mill, the service raises `RemovalException`, and the player must remove an opponent's piece.

The game transitions to Phase 2 when both players have placed all their pieces.

### Phase 2 — Movement

Players move their pieces to adjacent empty positions, according to the board's adjacency relationships.

A move that forms a mill triggers the piece-removal interaction.

### Phase 3 — Flying

When a player has exactly three pieces remaining on the board, that player can move a piece to any empty position rather than only to an adjacent one.

The service checks whether a player has fewer than three pieces or has no legal moves when determining whether the game has ended.

## 5. Main Interaction Flow

The general flow of a game is:

1. The application initializes the board, players, and game service.
2. The user chooses the console or graphical interface.
3. The interface reads the player's action.
4. The action is passed to `GameService`.
5. The service validates the action and updates the game state.
6. If a mill is formed, the interface handles the required piece removal.
7. The turn changes and the next player acts.
8. The game continues until a winning condition is reached.

In the graphical version, the computer player uses `MinimaxAI` to select its actions.

## 6. Design Considerations

The separation between the domain, service, and interface layers provides several benefits:

- **Separation of concerns:** Each component has a clearly defined responsibility.
- **Reusability:** The same game service is used by both interfaces.
- **Maintainability:** Changes to the interface do not require rewriting the core game rules.
- **Testability:** The board and service logic can be tested independently of the graphical interface.
- **Extensibility:** Additional interfaces or AI improvements can be introduced without redesigning the entire application.