package p322

import (
	"testing"
)

type testCase struct {
}

var (
	testCases = []testCase{}
)

func TestAll(t *testing.T) {
	t.Log(coinChange([]int{1, 2, 5}, 11))
	t.Log(coinChange([]int{2}, 3))
	t.Log(coinChange([]int{1}, 0))
	t.Log(coinChange([]int{1}, 1))
	t.Log(coinChange([]int{1}, 2))
}
