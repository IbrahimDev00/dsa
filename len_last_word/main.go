import "strings"
func lengthOfLastWord(s string) int {
    s = strings.TrimSpace(s)
    newS := strings.Split(s, " ")
    l := len(newS)
    res := len(newS[l-1])
	return res
}