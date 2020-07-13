package swap

import "strings"

// Moves returns the number of moves needed to turn one string into another
//
// If the strings are impossible to convert, return -1 (this is NOT idiomatic go)
//
// The strategy used here is to swap characters until the first character
// matches. Then repeat the process for the remaining characters.
//
// Example:
//
// in = dcab
// out = abcd
// expected moves = 5
//
// START    | dcab <- start by moving "a" to the front
// STEP 1   | dacb
// STEP 2   | adcb <- Now "a" is first. Next, move "b" to position 2
// STEP 3   | adbc
// STEP 4   | abdc <- Now "ab" is correct, next move "c" to the third position
// STEP 5   | abcd
//
// Because we only need to return the number of moves, we can take a
// computational shortcut. The number of moves to get "a" into the correct
// position is equal to its index. In the example above, a is the third letter
// (index 2), so we know that it takes 2 moves to get it into position.
//
// Once the a is in position, we can ignore it while calculating future moves
// because it doesn't need to move again. The problem is reduced to converting
// "dcb" -> "bcd" after the "a" is in the correct position.
//
// challenge found on dev.to:
// https://dev.to/thepracticaldev/daily-challenge-268-swapping-characters-in-strings-4n1g
func Moves(in, out string) int {
	if len(in) != len(out) {
		panic("invalid input, in must be same length as out")
	}
	if !isConvertable(in, out) {
		return -1
	}
	var moves, m int
	for _, c := range out {
		m, in = fixFirst(c, in)
		moves += m
	}
	return moves
}

// fixFirst returns the number of moves to put a rune at the start of `in`.
//
// It also returns `in` without the moved rune.
func fixFirst(r rune, in string) (int, string) {
	i := strings.IndexRune(in, r)
	s := strings.SplitAfterN(in, string(r), 2)
	// remove rune (it's the last item in the first string)
	s[0] = s[0][:len(s[0])-1]
	return i, strings.Join(s, "")
}

// isConvertable checks if in and out have the same characters.
//
// If the characters aren't the same, then no amount of character moves
// will be able to convert in to out.
func isConvertable(in, out string) bool {
	charDiff := map[rune]int{}
	for _, c := range in {
		charDiff[c] += 1
	}
	for _, c := range out {
		charDiff[c] -= 1
	}
	for _, freq := range charDiff {
		if freq != 0 {
			// TODO: return info about which rune caused the strings to
			// be inconvertable
			return false
		}
	}
	return true
}
