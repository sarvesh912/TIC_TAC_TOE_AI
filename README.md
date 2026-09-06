# TIC_TAC_TOE_AI
A Python-based Tic-Tac-Toe game featuring an AI opponent powered by the Minimax algorithm, allowing users to play against an intelligent and unbeatable computer player.
# 🎮 Tic-Tac-Toe AI in Python

A **Tic-Tac-Toe game built with Python** where a human player competes against an AI opponent.

The AI uses the **Minimax algorithm** to evaluate possible moves and choose the best move. This makes the AI capable of playing strategically and, with optimal play, preventing the human player from winning.

## 📌 Features

* 🎮 Human vs AI gameplay
* 🤖 AI opponent using the Minimax algorithm
* 🧠 Intelligent move selection
* ❌ Human plays as `X`
* ⭕ AI plays as `O`
* 🔢 Simple 1–9 position-based input
* ⚠️ Handles invalid user input
* 🚫 Prevents moves on occupied positions
* 🏆 Detects wins
* 🤝 Detects draws
* 💻 Runs directly in the terminal

## 🛠️ Technologies Used

* **Python 3**
* `math` module
* Minimax algorithm
* Terminal/Command Line Interface

## 📂 Project Structure

```text
Tic-Tac-Toe-AI/
│
├── tic_tac_toe.py
└── README.md
```

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/your-username/Tic-Tac-Toe-AI.git
```

### 3. Open the project folder

```bash
cd Tic-Tac-Toe-AI
```

### 4. Run the program

```bash
python tic_tac_toe.py
```

## 🎯 How to Play

The board contains 9 positions:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

You play as **X**.

The AI plays as **O**.

When asked:

```text
Your move (1-9):
```

Enter the number of the position where you want to place your `X`.

### Example

```text
Your move (1-9): 5

 X | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | O
```

The AI automatically calculates its next move.

## 🧠 How the AI Works

The AI uses the **Minimax algorithm**.

Minimax explores possible future moves and assigns scores to different game outcomes.

The scoring system used in this project is:

```text
AI wins     → positive score
Human wins  → negative score
Draw        → 0
```

The AI tries to **maximize its score**, while assuming that the human player will try to **minimize the AI's score**.

### Minimax concept

```text
                 Current Board
                      │
             ┌────────┼────────┐
             ▼        ▼        ▼
           Move 1   Move 2   Move 3
             │        │        │
             ▼        ▼        ▼
          Future    Future    Future
          Moves     Moves     Moves
             │        │        │
             └────────┼────────┘
                      ▼
                Best Move
```

The program recursively evaluates possible game states until it reaches a win, loss, or draw.

## 🔍 Important Functions

### `print_board()`

Displays the current Tic-Tac-Toe board.

### `winner()`

Checks all possible winning combinations:

* Rows
* Columns
* Main diagonal
* Secondary diagonal

### `game_over()`

Checks whether the game has ended.

### `minimax()`

Recursively evaluates possible moves and calculates the best score for the AI.

### `best_move()`

Tests available positions and selects the move with the highest Minimax score.

### `play()`

Controls the complete game:

```text
Start Game
    ↓
Human Move
    ↓
Check Win/Draw
    ↓
AI Calculates Best Move
    ↓
AI Move
    ↓
Check Win/Draw
    ↓
Repeat
```

## 🎓 Learning Objectives

This project demonstrates several important Python and computer science concepts:

* Functions
* Lists
* Loops
* Conditional statements
* Exception handling
* User input
* Recursion
* Algorithm design
* Game logic
* Artificial intelligence fundamentals
* Decision-making algorithms

## 🤖 Artificial Intelligence Concept

The project demonstrates a basic **game-playing AI**.

Instead of selecting a random position, the AI considers possible future outcomes and chooses a move based on the Minimax algorithm.

This introduces important AI concepts such as:

* State-space search
* Recursive decision making
* Maximizing and minimizing
* Game trees
* Evaluation functions

## 🔮 Future Improvements

Possible improvements include:

* Add difficulty levels
* Add Human vs Human mode
* Add AI vs AI mode
* Create a graphical interface using Tkinter
* Add sound effects
* Add score tracking
* Add restart functionality
* Improve the interface
* Add alpha-beta pruning for more efficient searching

## 👨‍💻 Author

**Sarvesh K**

Computer Science Engineering Student

## 📄 License

This project is created for educational and learning purposes.
