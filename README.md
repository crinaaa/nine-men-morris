# Nine Men's Morris

A Python implementation of the classic **Nine Men's Morris** board game, featuring both a graphical and a console interface, as well as a computer opponent powered by the Minimax algorithm.

## Game Rules

Nine Men's Morris is a two-player strategy board game. Each player starts with nine pieces and aims to reduce the opponent's pieces to fewer than three or prevent them from making a legal move.

The game consists of three phases:

1. **Placement Phase:** Players take turns placing their pieces on empty positions on the board.
2. **Movement Phase:** Once all pieces have been placed, players take turns moving one of their pieces to an adjacent empty position.
3. **Flying Phase:** When a player has only three pieces left, they can move a piece to any empty position on the board.

Forming a *mill* — a row of three pieces belonging to the same player — allows that player to remove one of the opponent's pieces, subject to the game's removal rules.

The game ends when a player has fewer than three pieces remaining or cannot make a legal move.

## Features

- **Two interfaces:** Play through a graphical interface built with Pygame or through the console.
- **Three game phases:** Piece placement, regular movement, and flying.
- **Mill detection:** Form a mill by aligning three pieces and remove an opponent's piece.
- **Move validation:** The game checks placements, movement, and piece-removal rules.
- **AI opponent:** Play against a computer player that uses depth-limited Minimax and a heuristic board evaluation.
- **Modular architecture:** Game logic, domain models, user interfaces, and AI are separated into dedicated modules.

## Technologies

- Python
- Pygame
- Object-Oriented Programming
- Minimax algorithm
- Unit testing with `unittest`

## Getting Started

### Prerequisites

- Python installed on your system.
- `pip`, Python's package installer.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/crinaaa/nine-men-morris.git
   cd nine-men-morris
   ```

2. Install the required dependency:

   ```bash
   python -m pip install pygame
   ```

### Running the Game

Start the application from the project's root directory:

```bash
python start_game/start.py
```

Enter your player name and choose between the console and graphical interfaces.

## Project Structure

```text
nine-men-morris/
│
├── domain/
│   ├── board.py
│   └── player.py
│
├── service/
│   └── game_service.py
│
├── start_game/
│   ├── minmax.py
│   └── start.py
│
├── gui/
│   └── nine_morris_gui.py
│
├── user_interface/
│   └── ui.py
│
├── exceptions/
│   └── exception_module.py
│
└── tests/
    ├── test_minmax.py
    ├── phase1.py
    ├── phase2.py
    └── phase3.py
```

## AI Opponent

The computer opponent uses a depth-limited **Minimax algorithm** to evaluate possible moves and select one with the highest estimated score.

The default search depth is 4. Its heuristic evaluation considers:

- Difference in the number of pieces on the board.
- Number of available moves (mobility).
- Completed mills.
- Potential mills.
- Terminal-like board conditions.

The AI implementation and its evaluation strategy are described in [docs/minimax.md](docs/minimax.md).

## Testing

The project includes tests for the three game phases and the Minimax implementation. The tests cover move validation, mill formation, piece removal, phase transitions, move generation, board evaluation, and simulation/undo operations.

To run the tests, see [docs/testing.md](docs/testing.md).

## Documentation

- [Architecture](docs/architecture.md)
- [Minimax AI](docs/minimax.md)
- [Testing](docs/testing.md)

## Future Improvements

- Improve the AI search strategy and its handling of game phases.
- Add further automated tests for complete game scenarios.
- Refine the graphical interface and add more game feedback.

---

This project was developed as an exercise in object-oriented programming, software architecture, algorithmic problem-solving, and game AI.


## Screenshots
<img src="screenshots/main-game.png" width="600">
