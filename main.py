from examples import *
from puzzle import EightPuzzle

if __name__ == '__main__':
    EightPuzzle(puzzle_5).solve_8puzzle('misplaced_tiles')
    # EightPuzzle(puzzle_5).solve_8puzzle('manhattan_distance')
    # EightPuzzle(EightPuzzle.random_puzzle_generator()).solve_8puzzle('manhattan_distance')
