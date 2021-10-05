package p756

import (
	"testing"
)

type testCase struct {
	input1 string
	input2 []string

	output1 bool
}

var (
	testCases = []testCase{
		{"BCD", []string{"BCG", "CDE", "GEA", "FFF"}, true},
		{"AABA", []string{"AAA", "AAB", "ABA", "ABB", "BAC"}, false},
		{"AABA", []string{"AAA", "AAB", "ABA", "ABB", "BAC", "BAA"}, true},
	}
)

func TestAll(t *testing.T) {
	for i, test := range testCases {
		expected := test.output1
		result := pyramidTransition(test.input1, test.input2)
		if expected != result {
			t.Errorf("Case %v: %v, %v\nexpected: %v\nresult: %v", i, test.input1, test.input2, expected, result)
		}
	}
}
