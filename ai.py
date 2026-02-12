class MinimaxAI:
    def __init__(self, ai_player="O", human_player="X"):
        self.ai = ai_player
        self.human = human_player

    def check_winner(self, state):
        # rows
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] != " ":
                return state[i][0]

        # columns
        for i in range(3):
            if state[0][i] == state[1][i] == state[2][i] != " ":
                return state[0][i]

        # diagonals
        if state[0][0] == state[1][1] == state[2][2] != " ":
            return state[0][0]

        if state[0][2] == state[1][1] == state[2][0] != " ":
            return state[0][2]

        # draw
        if all(cell != " " for row in state for cell in row):
            return "Draw"

        return None

    def minimax(self, state, is_maximizing):
        result = self.check_winner(state)

        if result == self.ai:
            return 1
        if result == self.human:
            return -1
        if result == "Draw":
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if state[i][j] == " ":
                        state[i][j] = self.ai
                        score = self.minimax(state, False)
                        state[i][j] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if state[i][j] == " ":
                        state[i][j] = self.human
                        score = self.minimax(state, True)
                        state[i][j] = " "
                        best_score = min(best_score, score)
            return best_score

    def best_move(self, state):
        best_score = -float("inf")
        move = None

        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    state[i][j] = self.ai
                    score = self.minimax(state, False)
                    state[i][j] = " "

                    if score > best_score:
                        best_score = score
                        move = (i, j)

        return move

