# Maze Generator using Depth-First Search (DFS)

This Python project generates a maze using the Depth-First Search (DFS) algorithm. The maze is created within a grid and visualized in the terminal. Each maze cell is surrounded by walls, and DFS carves out a path through the grid.

## How It Works

1. **Grid Creation**: 
   - The maze is represented as a 2D grid where cells are enclosed by walls (`+`, `---`, `|`).
   - The function `create_grid()` initializes the maze grid with walls and empty spaces for cells.

2. **Maze Generation**: 
   - The function `generate_maze()` generates the maze using the DFS algorithm.
   - Starting from the top-left cell `(1, 1)`, the algorithm explores all neighboring cells randomly, carving paths by removing walls between adjacent cells.
   - The DFS algorithm ensures that all cells in the maze are visited, resulting in a perfect maze without loops.

## Code Structure

- `create_grid(rows, cols)`: 
  - Creates a grid with the specified number of rows and columns.
  - Each cell is initially surrounded by walls, and the placeholders "0" represent cells to be carved into the maze.

- `generate_maze(rows, cols)`:
  - Uses Depth-First Search (DFS) to generate the maze by removing walls between neighboring cells.
  - Carves paths between cells as the algorithm explores and visits new cells.

## Example Output

For a 5x5 maze grid, the generated output would look something like this:

```
+---+---+---+---+---+
|       |           |
+---+   +   +---+   +
|   |       |   |   |
+   +---+---+   +   +
|               |   |
+   +---+---+---+   +
|               |   |
+   +---+---+   +   +
|           |       |
+---+---+---+---+---+
```


This shows the paths between cells and walls, representing a solvable maze.

## Usage

### Prerequisites

- Python 3.x is required to run the code.

### Running the Code

1. Clone the repository or copy the code into a Python file (e.g., `maze.py`).
2. Run the Python script to generate a maze:
   ```bash
   python maze.py
   ```
3. The maze will be printed to the terminal.

### Customizing the maze size

You can change the dimensions of the maze by modifying the arguments passed to `generate_maze()`. For example:

```bash
mz = generate_maze(10, 10)
```

This will generate a 10x10 maze.

