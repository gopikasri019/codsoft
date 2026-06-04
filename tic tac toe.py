import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("🤖 AI Tic-Tac-Toe")
root.geometry("600x720")
root.configure(bg="#0A0F2C")
root.resizable(False, False)

CELL = 120
BOARD_SIZE = 360

board = [""] * 9
player_score = 0
ai_score = 0
draw_score = 0
game_over = False

difficulty = tk.StringVar(root, value="Medium")

title = tk.Label(root, text="⚡ AI TIC-TAC-TOE",
                 font=("Segoe UI", 22, "bold"),
                 bg="#0A0F2C", fg="white")
title.pack(pady=8)

tk.Label(root, text="Human vs AI",
         font=("Segoe UI", 12),
         bg="#0A0F2C", fg="#66B3FF").pack()

score_var = tk.StringVar(value="😊 Player: 0    🤖 AI: 0    🤝 Draws: 0")

tk.Label(root, textvariable=score_var,
         font=("Segoe UI", 12, "bold"),
         bg="#201060", fg="white",
         padx=15, pady=8).pack(pady=10)

status_var = tk.StringVar(value="😊 Your Turn (X)")

tk.Label(root, textvariable=status_var,
         font=("Segoe UI", 16, "bold"),
         bg="#0A0F2C", fg="#39FF88").pack(pady=5)

difficulty_frame = tk.Frame(root, bg="#0A0F2C")
difficulty_frame.pack(pady=5)

tk.Label(difficulty_frame, text="🎮 Difficulty:",
         font=("Segoe UI", 12, "bold"),
         bg="#0A0F2C", fg="white").pack(side="left", padx=5)

difficulty_menu = tk.OptionMenu(
    difficulty_frame, difficulty,
    "Easy", "Medium", "Hard", "Impossible"
)
difficulty_menu.config(font=("Segoe UI", 11), width=10)
difficulty_menu.pack(side="left")

canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE,
                   bg="#12003A", highlightthickness=3,
                   highlightbackground="#FF4DFF")
canvas.pack(pady=15)

def draw_board():
    canvas.delete("grid")
    for i in range(1, 3):
        canvas.create_line(0, i*CELL, BOARD_SIZE, i*CELL,
                           fill="#FF4DFF", width=4, tags="grid")
        canvas.create_line(i*CELL, 0, i*CELL, BOARD_SIZE,
                           fill="#FF4DFF", width=4, tags="grid")

def check_winner(brd):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if brd[a] == brd[b] == brd[c] and brd[a] != "":
            return brd[a]
    if "" not in brd:
        return "Draw"
    return None

def minimax(brd, maximizing):
    result = check_winner(brd)
    if result == "O": return 1
    if result == "X": return -1
    if result == "Draw": return 0

    if maximizing:
        best = -999
        for i in range(9):
            if brd[i] == "":
                brd[i] = "O"
                best = max(best, minimax(brd, False))
                brd[i] = ""
        return best
    else:
        best = 999
        for i in range(9):
            if brd[i] == "":
                brd[i] = "X"
                best = min(best, minimax(brd, True))
                brd[i] = ""
        return best

def best_move():
    best_score = -999
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def random_move():
    available = [i for i in range(9) if board[i] == ""]
    return random.choice(available) if available else None

def draw_symbol(index, symbol):
    row, col = divmod(index, 3)
    x = col * CELL + CELL // 2
    y = row * CELL + CELL // 2
    color = "#66B3FF" if symbol == "X" else "#FF7B39"
    canvas.create_text(x, y, text=symbol,
                       font=("Segoe UI", 50, "bold"),
                       fill=color)

def update_score():
    score_var.set(
        f"😊 Player: {player_score}    🤖 AI: {ai_score}    🤝 Draws: {draw_score}"
    )

def reset_board():
    global board, game_over
    board = [""] * 9
    game_over = False
    canvas.delete("all")
    draw_board()
    status_var.set("😊 Your Turn (X)")

def end_game(result):
    global player_score, ai_score, draw_score, game_over
    game_over = True

    if result == "X":
        player_score += 1
        messagebox.showinfo("Winner", "🎉 You Won!")
    elif result == "O":
        ai_score += 1
        messagebox.showinfo("Winner", "🤖 AI Wins!")
    else:
        draw_score += 1
        messagebox.showinfo("Draw", "🤝 Match Draw!")

    update_score()
    reset_board()

def ai_move():
    if game_over:
        return

    level = difficulty.get()

    if level == "Easy":
        move = random_move()
    elif level == "Medium":
        move = best_move() if random.random() < 0.7 else random_move()
    elif level == "Hard":
        move = best_move() if random.random() < 0.9 else random_move()
    else:
        move = best_move()

    if move is not None:
        board[move] = "O"
        draw_symbol(move, "O")

    result = check_winner(board)
    if result:
        end_game(result)
    else:
        status_var.set("😊 Your Turn (X)")

def click(event):
    if game_over:
        return

    col = event.x // CELL
    row = event.y // CELL
    idx = row * 3 + col

    if idx < 9 and board[idx] == "":
        board[idx] = "X"
        draw_symbol(idx, "X")

        result = check_winner(board)
        if result:
            end_game(result)
            return

        status_var.set("🤖 AI Thinking...")
        root.after(300, ai_move)

canvas.bind("<Button-1>", click)

tk.Button(root, text="🔄 NEW GAME",
          font=("Segoe UI", 12, "bold"),
          bg="#8A2BE2", fg="white",
          command=reset_board).pack(pady=10)

tk.Label(root,
         text="CodSoft Artificial Intelligence Internship Project",
         bg="#0A0F2C", fg="#AAB8FF",
         font=("Segoe UI", 10)).pack(pady=5)

draw_board()
root.mainloop()