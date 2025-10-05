def find_path(grid, start, end):
    """
    Return a list of (r,c) from start to end inclusive, or None if no path.
    grid contains 0 (open) and 1 (wall). Moves: up/down/left/right.
    """
    # TODO: implement recursively with backtracking
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def _solve(current):
        r, c = current

        # Check if out of bounds, a wall, or already visited on this path
        if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and current not in visited):
            return None

        # Base case: We have reached the end
        if current == end:
            return [end]

        # Mark the current cell as visited for this attempt
        visited.add(current)

        # Explore neighbors (Right, Left, Down, Up)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            path = _solve((r + dr, c + dc))
            if path:
                # If a neighbor found the end, prepend ourself and return success
                return [current] + path

        # Backtrack: No path was found from here. Un-mark the cell so other paths can use it.
        visited.remove(current)
        
        return None

    return _solve(start)

