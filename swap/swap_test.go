package swap_test

import (
	"testing"

	"github.com/cstoltze/puzzles/swap"
)

func TestMoves(t *testing.T) {
	tests := []struct {
		name    string
		in, out string
		want    int
	}{
		{
			name: "inconvertable",
			in:   "b",
			out:  "a",
			want: -1,
		},
		{
			name: "identical",
			in:   "abc",
			out:  "abc",
			want: 0,
		},
		{
			name: "1 swap",
			in:   "ba",
			out:  "ab",
			want: 1,
		},
		{
			name: "5 swap",
			in:   "dcab",
			out:  "abcd",
			want: 5,
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := swap.Moves(test.in, test.out)
			if got != test.want {
				t.Fatalf("got: %d, want %d", got, test.want)
			}
		})
	}
}
