/*
For each "1", check its neighbors and update perimeter accordingly.
*/
func islandPerimeter(grid [][]int) int {
    perimeter := 0
    delta := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == 1 {
                perimeter += 4
                for _, d := range delta {
                    x, y := i + d[0], j + d[1]
                    if 0 <= x && x < len(grid) && 0 <= y && y < len(grid[0]) {
                        perimeter -= grid[x][y]
                    }
                }
            }
        }
    }
    return perimeter
}
