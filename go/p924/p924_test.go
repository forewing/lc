package p924

import (
	"testing"
)

type testCase struct {
}

var (
	testCases = []testCase{}
)

func TestAll(t *testing.T) {
	t.Log(minMalwareSpread(
		[][]int{
			{1, 0, 0, 0},
			{0, 1, 0, 0},
			{0, 0, 1, 1},
			{0, 0, 1, 1},
		},
		[]int{
			3, 1,
		},
	),
	)
}
