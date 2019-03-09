/*
Example: 3 + 7 = 10
 111b
  11b
===== res -> 100b, carryover -> 11b, shift the carryover 1-bit left
 100b
 110b
===== res -> 10b, carryover -> 100b, shift the carryover 1-bit left
  10b
1000b
===== res -> 1010b, carryover -> 0b
res is 10.
*/
func getSum(a int, b int) int {
    res, carryover := a^b, a&b
    for carryover != 0 {
        carryover = carryover << 1
        res, carryover = res^carryover, res&carryover
    }
    return res
}
