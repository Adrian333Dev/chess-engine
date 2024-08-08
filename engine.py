from typing import Tuple

CellPos = Tuple[int, int]


class Move:
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(
        self, start_cell: CellPos, end_cell: CellPos, board: list[list[str]]
    ) -> None:
        self.start_row = start_cell[0]
        self.start_col = start_cell[1]
        self.end_row = end_cell[0]
        self.end_col = end_cell[1]

        self.moved_piece = board[self.start_row][self.start_col]
        self.captured_piece = board[self.end_row][self.end_col]

        self.id = (
            self.start_row * 1000
            + self.start_col * 100
            + self.end_row * 10
            + self.end_col
        )

    def __eq__(self, value: object) -> bool:
        return isinstance(value, Move) and self.id == value.id

    def get_notation(self):
        return self.get_cell_rank_file(
            self.start_row, self.start_col
        ) + self.get_cell_rank_file(self.end_row, self.end_col)

    def get_cell_rank_file(self, row: int, col: int):
        return self.cols_to_files[col] + self.rows_to_ranks[row]


Moves = list[Move]


class GameState:
    def __init__(self) -> None:
        self.board: list[list[str]] = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.white_to_move = True
        self.move_logs: Moves = []

    def make_move(self, move: Move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.moved_piece
        self.move_logs.append(move)

    def undo_move(self):
        if not len(self.move_logs):
            print("No Move Found")
        else:
            move = self.move_logs.pop()
            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece
            self.white_to_move = not self.white_to_move

    def get_valid_moves(self):
        return self.get_all_moves()

    def get_all_moves(self) -> Moves:
        moves: Moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn, piece = self.board[row][col]
                if (turn == "w" and self.white_to_move) and (
                    turn == "b" and not self.white_to_move
                ):
                    match piece:
                        case "P":
                            self.get_pawn_moves(row, col, moves)
                        case "R":
                            self.get_rook_moves(row, col, moves)
                        case "N":
                            self.get_knight_moves(row, col, moves)
                        case "B":
                            self.get_bishop_moves(row, col, moves)
                        case "Q":
                            self.get_queen_moves(row, col, moves)
                        case "K":
                            self.get_king_moves(row, col, moves)
        return Moves

    def get_pawn_moves(row: int, col: int, moves: Moves):
        pass

    def get_rook_moves(row: int, col: int, moves: Moves):
        pass

    def get_knight_moves(row: int, col: int, moves: Moves):
        pass

    def get_bishop_moves(row: int, col: int, moves: Moves):
        pass

    def get_queen_moves(row: int, col: int, moves: Moves):
        pass

    def get_king_moves(row: int, col: int, moves: Moves):
        pass
