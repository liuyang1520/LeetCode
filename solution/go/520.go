/*
Use ToUpper, ToLower, Title for convenience
*/
func detectCapitalUse(word string) bool {
    if word == strings.ToUpper(word) {
        return true
    } else if word == strings.ToLower(word) {
        return true
    } else if word == strings.Title(strings.ToLower(word)) {
        return true
    }
    return false
}}
