from os.path import join
from typing import Dict, Tuple
import pygame as pg

pieces: Tuple[str] = ("R", "N", "B", "Q", "K", "P")


def load_asset(*path: str) -> pg.Surface:
    return pg.image.load(join("assets", *path))


def load_pieces(CELL_SIZE: int) -> Dict[str, pg.Surface]:
    images: Dict[str, pg.Surface] = {}

    def load_piece(PIECE_SRC: str):
        return pg.transform.scale(load_asset("pieces", PIECE_SRC), (CELL_SIZE, CELL_SIZE))

    for p in pieces:
        wPiece, bPiece = [f"w{p}", f"b{p}"]
        images[wPiece] = load_piece(f"{wPiece}.png")
        images[bPiece] = load_piece(f"{bPiece}.png")

    return images
