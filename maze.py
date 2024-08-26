import random

# Create a grid with 0s
def create_grid(rows, cols):
    
    r = rows * 2 + 1  # Calculate the number of rows in the maze grid
    c = cols * 2 + 1  # Calculate the number of columns in the maze grid
    grid = []

    for i in range(r):
        if i % 2 == 0:
            
            grid.append(["+"])  # Start with a corner "+"
            for j in range(cols):
                grid[i].append("---")  # Add horizontal wall sections
                grid[i].append("+")    # Add corners between wall sections
        else:
            
            row = ["|"]  # Start with a vertical wall "|"
            grid.append(row)
            for j in range(cols):
                grid[i].append(" 0 ")  # Add a cell with a placeholder "0"
                grid[i].append("|")    # Add vertical wall between cells

    return grid

# Generate the maze using Depth-First Search (DFS)
def generate_maze(rows, cols):
    maze = create_grid(rows, cols)  # Initialize the grid
    start = (1, 1)  # Starting point of the maze
    stack = [start]  # Stack to hold the path during DFS
    visited = set()  # Set to keep track of visited cells
    r = rows * 2 + 1
    c = cols * 2 + 1

    while stack:
        current = stack[-1]  # Current cell in the maze
        visited.add(current)  # Mark the current cell as visited
        x, y = current
        maze[x][y] = "   "  # Remove the placeholder of the current cell

        neighbors = []
        # Explore potential neighbors in the maze
        for i, j in [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]:
            if 0 <= i < r and 0 <= j < c and (i, j) not in visited:
                neighbors.append((i, j))

        if neighbors:
            # Choose a random neighbor to move to
            next_cell = neighbors[random.randint(0, len(neighbors)-1)]
            stack.append(next_cell)  # Add the chosen cell to the stack
            a, b = next_cell
            if a == x:
                # If moving horizontally, remove the wall between cells
                se = maze[x][min(y, b)+1]
                if se == '---':
                    maze[x][min(y, b)+1] = "   "  # Carve the horizontal wall
                else:
                    maze[x][min(y, b)+1] = " "  # Open the path between cells
            else:
                # If moving vertically, remove the wall between cells
                se = maze[min(x, a)+1][y]
                if se == '|':
                    maze[min(x, a)+1][y] = " "  # Carve the vertical wall
                else:
                    maze[min(x, a)+1][y] = "   "  # Open the path between cells
        else:
            # If no unvisited neighbors, backtrack
            stack.pop()
        
    return maze

# Generate a maze with specified dimensions
mz = generate_maze(20, 20)
for row in mz:
    print("".join(row))  # Print the maze row by row
