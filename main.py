import pygame as pg

from settings import *
from utils import load_pieces
from engine import GameState


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

    def run(self):
        while self.is_running:

            # Event Loop
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.is_running = False

            # Draw
            self.display_surf.fill("black")
            self.draw_game_state()
            self.clock.tick(30)
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

        for r in range(DIMENTIONS):
            for c in range(DIMENTIONS):
                pg.draw.rect(
                    self.display_surf,
                    WHITE if ((r + c) % 2) == 0 else BLACK,
                    self.cell_rect(r, c),
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
    def cell_rect(r: int, c: int) -> pg.FRect:
        return pg.FRect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)


if __name__ == "__main__":
    game = Game()
    game.run()
