/*
Modify the ops array in-place
*/
func calPoints(ops []string) int {
    for i := 0; i < len(ops); i++ {
        if ops[i] == "C" {
            ops = append(ops[:i-1], ops[i+1:]...)
            i -= 2
        } else if ops[i] == "D" {
            ops[i] = strconv.Itoa(strToInt(ops[i-1]) * 2)
        } else if ops[i] == "+" {
            ops[i] = strconv.Itoa(strToInt(ops[i-1]) + strToInt(ops[i-2]))
        }
    }
    sum := 0
    for _, val := range ops {
        sum += strToInt(val)
    }
    return sum
}

func strToInt(x string) int{
    if y, err := strconv.Atoi(x); err == nil {
        return y
    }
    return 0
}
