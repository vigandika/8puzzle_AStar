# 8puzzle_AStar

Solve any 8 Puzzle Problem using the A* algorithm. Choose one of the admissible heuristics such as 
* Manhattan Distance or 
* Misplaced Tiles
and see results.

# How to run
Place your 8 Puzzle in the `examples.py` in a form of a List e.g `exampleX = [2,3,1,0,4,7,8,5,6]` (Assign 0 to the free space).

Go to `main.py` and give your puzzle as an argument to the `EightPuzzle` method as well as apply the wanted heuristic.
```python3
EightPuzzle(exampleX).solve_8puzzle('manhattan_distance')
# or
EightPuzzle(exampleX).solve_8puzzle('misplaced_tiles')
# or generate a random puzzle using
EightPuzzle(EightPuzzle.random_puzzle_generator()).solve_8puzzle('misplaced_tiles')
```
