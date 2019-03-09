/*
BFS
*/
func canVisitAllRooms(rooms [][]int) bool {
    queue := []int{0}
    visited := map[int]bool{0: true}
    for ; len(queue) > 0; {
        temp := make([]int, 0)
        for _, val := range(queue) {
            accesses := rooms[val]
            for _, access := range(accesses) {
                if !visited[access] {
                    visited[access] = true
                    temp = append(temp, access)
                }
            }
        }
        queue = temp
    }
    if len(visited) == len(rooms) {
        return true
    } else {
        return false
    }
}
