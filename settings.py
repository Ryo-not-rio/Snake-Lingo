DISPLAY_SIZE = 800
NUM_ROWS_COLUMNS = 10
BLOCK_SIZE = int(DISPLAY_SIZE/NUM_ROWS_COLUMNS)

def grid_to_pos(grid_pos):
    return [BLOCK_SIZE*i for i in grid_pos]