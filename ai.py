#評価関数を用いて強くした
import math
import random

BLACK = 1
WHITE = 2

# 6×6の初期ボード
board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 0, 0],
    [0, 0, 2, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# 評価関数用の重み (コーナーが高い価値を持つ)
evaluation_weights = [
    [100, -20, 10, 10, -20, 100],
    [-20, -50, 1, 1, -50, -20],
    [10, 1, 5, 5, 1, 10],
    [10, 1, 5, 5, 1, 10],
    [-20, -50, 1, 1, -50, -20],
    [100, -20, 10, 10, -20, 100],
]

def can_place_x_y(board, stone, x, y):
    """
    指定された位置 (x, y) に石を置けるかを判定する。
    """
    if board[y][x] != 0:
        return False

    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True

    return False

def count_flippable_stones(board, stone, x, y):
    """
    指定された位置 (x, y) に石を置いた場合にひっくり返せる石の数を数える。
    """
    if board[y][x] != 0:
        return 0

    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_flippable = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        flippable = 0

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            flippable += 1

        if flippable > 0 and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            total_flippable += flippable

    return total_flippable

def evaluate_board(board, stone):
    """
    現在のボードの評価値を計算する。
    """
    score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                score += evaluation_weights[y][x]
            elif board[y][x] == (3 - stone):  # 相手の石
                score -= evaluation_weights[y][x]
    return score

def best_place(board, stone):
    """
    評価関数を使って最適な場所を探す関数。
    """
    best_score = -float('inf')
    best_move = None

    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                # 仮に石を置いてみる
                temp_board = [row[:] for row in board]
                temp_board[y][x] = stone
                # 評価関数でスコアを計算
                score = evaluate_board(temp_board, stone)
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    return best_move

class TyokokoroneAI(object):

    def face(self):
        return "🥐"

    def place(self, board, stone):
        # 最適な場所を探す
        move = best_place(board, stone)
        return move

!pip install -U kogi-canvas

from kogi_canvas import play_othello
play_othello(TyokokoroneAI())  # 強いAIをプレイに使う
