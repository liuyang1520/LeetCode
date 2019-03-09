/*
Pick up the first row and first column, compare all elements x+1, y+1.
*/
func isToeplitzMatrix(matrix [][]int) bool {
    //first row
    for j := 0; j < len(matrix[0]); j++ {
        x, y, cur := 0, j, matrix[0][j]
        for ; x < len(matrix) && y < len(matrix[0]); x, y = x+1, y+1 {
            if cur != matrix[x][y] {
                return false
            }
        }
    }
    //first column
    for i := 0; i < len(matrix); i++ {
        x, y, cur := i, 0, matrix[i][0]
        for ; x < len(matrix) && y < len(matrix[0]); x, y = x+1, y+1 {
            if cur != matrix[x][y] {
                return false
            }
        }
    }
    return true
}
