/*
Scan the letters linearly
*/
func nextGreatestLetter(letters []byte, target byte) byte {
    for i := 0; i < len(letters) - 1; i++ {
        if target >= letters[i] && target < letters[i+1] {
            return letters[i+1]
        }
    }
    return letters[0]
}
