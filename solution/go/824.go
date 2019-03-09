/*
Use a map to quickly look up the vowels.
*/
func toGoatLatin(S string) string {
    vowels := map[string]int{"a": 1, "e": 1, "i": 1, "o": 1, "u": 1,
                             "A": 1, "E": 1, "I": 1, "O": 1, "U": 1}

    words := strings.Split(S, " ")
    for i, word := range words {
        if _, ok := vowels[string(word[0])]; !ok {
            words[i] = word[1:] + string(word[0])
        }
        words[i] += "ma" + strings.Repeat("a", i + 1)
    }

    return strings.Join(words, " ")
}
