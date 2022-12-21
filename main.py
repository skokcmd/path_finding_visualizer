import pygame

from node import Grid
from io_service import handle_input
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, NODE_GRID_SIDE_SIZE, RUNTIME_ARGS_COUNT

def main() -> None:
    window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    canvas = Grid(NODE_GRID_SIDE_SIZE, window)

    # [0] = is_start
    # [1] = is_end
    # [2] = is_running
    runtime = [False] * RUNTIME_ARGS_COUNT
    while True:
        canvas.draw_grid_with_nodes()
        for event in pygame.event.get():
            handle_input(event, canvas, runtime, canvas.start_position, canvas.end_position)


if __name__ == "__main__":
    main()