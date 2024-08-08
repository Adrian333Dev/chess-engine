import pygame as pg

from settings import *
from utils import load_pieces
from engine import GameState, Move

from sl_chess.piece import Piece


class Game:
    def __init__(self) -> None:
        # Setup
        pg.init()
        self.display_surf = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Chess Game")
        self.piece_imgs = load_pieces(CELL_SIZE)
        self.game_state = GameState()
        self.clock = pg.time.Clock()
        self.is_running = True
        self.selected_cell = ()
        self.clicks = []
        self.valid_moves = self.game_state.get_valid_moves()
        self.move_made = False

    def run(self):
        while self.is_running:

            # Event Loop
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.is_running = False
                elif e.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    col, row = [pos[0] // CELL_SIZE, pos[1] // CELL_SIZE]
                    if self.selected_cell == (row, col):
                        self.selected_cell = ()
                        self.clicks = []
                    else:
                        self.selected_cell = (row, col)
                        self.clicks.append(self.selected_cell)

                    if len(self.clicks) == 2:
                        move = Move(
                            self.clicks[0], self.clicks[1], self.game_state.board
                        )
                        if move in self.valid_moves:
                            self.game_state.make_move(move)
                            self.move_made = True
                        self.selected_cell = ()
                        self.clicks = []
                        print(f"CHESS NOTATION: {move.get_notation()}")
                elif e.type == pg.KEYDOWN:
                    if e.key == pg.K_z:
                        self.game_state.undo_move()
                        self.move_made = True

            if self.move_made:
                self.valid_moves = self.game_state.get_valid_moves()
                self.move_made = False

            # Draw
            self.display_surf.fill("black")
            self.draw_game_state()
            self.clock.tick(MAX_FPS)
            pg.display.update()

        pg.quit()

    def update():
        pass

    def draw_game_state(self):
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        curr_x = 0
        curr_y = 0

        for row in range(DIMENTIONS):
            for col in range(DIMENTIONS):
                color = COLORS[
                    ((row + col) % 2) + (2 if self.selected_cell == (row, col) else 0)
                ]
                pg.draw.rect(
                    self.display_surf,
                    color,
                    self.cell_rect(row, col),
                )
                curr_x += CELL_SIZE
            curr_x = 0
            curr_y += CELL_SIZE

    def draw_pieces(self):
        for r in range(DIMENTIONS):
            for c in range(DIMENTIONS):
                piece = self.game_state.board[r][c]
                if piece != "--":
                    self.display_surf.blit(
                        self.piece_imgs[piece],
                        self.cell_rect(r, c),
                    )

    # Utils
    def cell_rect(self, r: int, c: int) -> pg.FRect:
        return pg.FRect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)


if __name__ == "__main__":
    game = Game()
    game.run()
