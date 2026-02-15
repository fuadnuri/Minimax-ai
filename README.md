# Hello welcome to minmax ai player of tiktactoe player
** AI always wins or it's a draw 

```markdown
# Minimax AI

A high-performance implementation of the Minimax algorithm served via FastAPI. This project provides an API interface to calculate optimal moves for game-theory-based scenarios.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone [https://github.com/fuadnuri/minimax-ai](https://github.com/fuadnuri/minimax-ai)
cd minimax-ai

```
### 1. Just copy the `.ipynb` file to your jupitor nobebook and run it for command line testing 
### Or open the `index.html` file to test it in web based invironment. follow steps below.
### 2. Environment Setup

Create a virtual environment to keep your project dependencies isolated.

| Platform | Command to Create | Command to Activate |
| --- | --- | --- |
| **Linux / macOS** | `python3 -m venv venv` | `source venv/bin/activate` |
| **Windows** | `python -m venv venv` | `.\venv\Scripts\activate` |

> **💡 Windows Tip:** If you get an error about "scripts are disabled on this system," run PowerShell as Administrator and execute:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### 3. Install Dependencies

Once your virtual environment is active, install the required packages:

```bash
pip install -r requirements.txt

```

### 4. Run the Application

Start the FastAPI server using the following command:

```bash
fastapi run main.py

```

---
## then open the index.html 

## 🧠 How Minimax Works

The Minimax algorithm is a decision-making tool used in game theory to find the optimal move for a player, assuming that the opponent is also playing optimally.

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Logic:** Minimax Algorithm (Recursive backtracking)
