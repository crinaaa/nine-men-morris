# Testing

## 1. Overview

The project uses Python's built-in `unittest` framework to test the game logic and the Minimax implementation.

The tests are organized into four files:

| Test file | Main focus |
|---|---|
| `test_minmax.py` | AI evaluation, move generation, simulation, and Minimax |
| `phase1.py` | Piece placement and mill formation |
| `phase2.py` | Regular movement and move validation |
| `phase3.py` | Flying rules and movement validation |

The tests focus on the domain and service logic rather than the graphical interface.

## 2. Running the Tests

Run the following commands from the project's root directory:

### Minimax tests

```bash
python -m unittest discover -s tests -p "test_minmax.py"
```

### Phase 1 tests — Placement

```bash
python -m unittest discover -s tests -p "phase1.py"
```

### Phase 2 tests — Movement

```bash
python -m unittest discover -s tests -p "phase2.py"
```

### Phase 3 tests — Flying

```bash
python -m unittest discover -s tests -p "phase3.py"
```

## 3. Test Coverage

### 3.1 Minimax — `test_minmax.py`

These tests verify the AI's main operations.

They cover:

- Evaluation of an empty board.
- Positive evaluation when the AI has a piece advantage.
- Negative evaluation when the opponent has a piece advantage.
- Generation of placement moves.
- Generation of adjacent movement moves.
- Simulation and undo of a move.
- Selection of a valid move.
- Simulation of opponent-piece removal after a mill.
- Detection of a game-over condition.

### 3.2 Phase 1 — `phase1.py`

These tests focus on the placement phase.

They verify:

- Successful placement of a piece.
- Rejection of an occupied position.
- Rejection of invalid board positions.
- Detection of a mill after placement.
- Restrictions on removing an opponent's piece that belongs to a mill.
- Transition to the movement phase after both players have placed all their pieces.

### 3.3 Phase 2 — `phase2.py`

These tests focus on regular piece movement.

They verify:

- Successful movement to an adjacent position.
- Rejection of non-adjacent movement.
- Prevention of moving an opponent's piece.
- Prevention of moving onto an occupied position.
- Detection of a mill formed through movement.
- Allowing a player with three pieces to move to a non-adjacent empty position.

### 3.4 Phase 3 — `phase3.py`

These tests focus on the flying phase.

They verify:

- Allowing a player with three pieces to move to any empty position.
- Preventing a player with more than three pieces from moving to a non-adjacent position.
- Preventing a player from moving an opponent's piece.
- Preventing movement onto an occupied position.
- Detecting a mill formed during a flying move.

## 4. Testing Approach

The tests use `setUp()` to create fresh players, a board, and a game service before each test.

This keeps individual tests independent and prevents state changes from one test from affecting another.

The tests use assertions such as:

- `assertEqual()` to compare expected and actual values.
- `assertTrue()` to verify a condition.
- `assertIn()` to check whether a value belongs to a collection.
- `assertRaises()` to verify that invalid actions trigger the expected exception.

Together, these tests provide coverage of the main game phases, important validation rules, and the AI's basic functionality.