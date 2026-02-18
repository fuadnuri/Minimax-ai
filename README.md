# 🎮 Minimax AI — Tic-Tac-Toe

> **The AI always wins — or forces a draw. No exceptions.**

A high-performance implementation of the **Minimax algorithm** served via **FastAPI**, with both a web-based UI and a Jupyter notebook interface. The AI plays perfectly by recursively exploring every possible game state and choosing the optimal move every time.

---

## ✨ Features

- 🧠 **Unbeatable AI** — powered by the Minimax algorithm with full game-tree search
- ⚡ **FastAPI backend** — fast, async, and auto-documented via Swagger UI
- 🌐 **Web interface** — open `index.html` and play instantly in your browser
- 📓 **Jupyter Notebook** — test the algorithm directly from the command line
- 🔁 **Optimal play guaranteed** — always wins or draws, never loses

---

## 🚀 Getting Started

### Option A — Web Interface (Recommended)

**1. Clone the repository**
```bash
git clone https://github.com/fuadnuri/minimax-ai
cd minimax-ai
```

**2. Create and activate a virtual environment**

| Platform | Create | Activate |
|---|---|---|
| Linux / macOS | `python3 -m venv venv` | `source venv/bin/activate` |
| Windows | `python -m venv venv` | `.\venv\Scripts\activate` |

> 💡 **Windows Tip:** If you see a script execution error, open PowerShell as Administrator and run:
> ```
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Start the FastAPI server**
```bash
fastapi run main.py
```

**5. Open the UI**

Open `index.html` in your browser and start playing!

> The API docs are also available at `http://localhost:8000/docs`

---

### Option B — Jupyter Notebook

Copy the `.ipynb` file into your Jupyter environment and run the cells for command-line testing — no server setup needed.

---

## 🧠 How Minimax Works

Minimax is a recursive decision-making algorithm from game theory. It simulates every possible move in the game and picks the one that **maximizes the AI's outcome** while assuming the opponent also plays perfectly.

```
                    [Current Board]
                   /               \
            [AI Move A]         [AI Move B]
           /     \                /     \
     [Opp A1] [Opp A2]     [Opp B1] [Opp B2]
        ...      ...           ...      ...
       WIN      DRAW          LOSE      WIN
```

At each level, the AI alternates between:
- **Maximizing** its own score (AI's turn)
- **Minimizing** the opponent's score (opponent's turn)

The result: the AI always selects the path that leads to the best guaranteed outcome — making it impossible to beat.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Algorithm | Minimax (Recursive Backtracking) |
| Interface | HTML/CSS/JS + Jupyter Notebook |

---

## 📁 Project Structure

```
minimax-ai/
├── main.py          # FastAPI app & Minimax logic
├── index.html       # Web-based game interface
├── minimax.ipynb    # Jupyter notebook for CLI testing
├── requirements.txt # Python dependencies
└── README.md
```

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/move` | Get the AI's optimal next move |
| `GET` | `/docs` | Interactive Swagger API documentation |

---

## 📄 License

This project is open source. See `LICENSE` for details.
