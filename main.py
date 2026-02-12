from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .ai import MinimaxAI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
ai = MinimaxAI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class BoardRequest(BaseModel):
    board: List[List[str]]


class MoveResponse(BaseModel):
    board: List[List[str]]
    winner: str | None


@app.post("/move", response_model=MoveResponse)
def make_move(data: BoardRequest):
    board = data.board

    # Check if user already won
    winner = ai.check_winner(board)
    if winner:
        return {"board": board, "winner": winner}

    # AI move
    move = ai.best_move(board)
    if move:
        i, j = move
        board[i][j] = "O"

    # Check again after AI move
    winner = ai.check_winner(board)

    return {
        "board": board,
        "winner": winner
    }
