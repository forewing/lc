package p556

import (
	"testing"
)

type testCase struct {
}

var (
	testCases = []testCase{}
)

func TestAll(t *testing.T) {
	// for i, test := range testCases {
	// 	expected :=
	// 	result :=
	// 	if expected != result {
	// 	 t.Errorf("Case %v: %v\nexpected: %v\nresult: %v", i, test.input1, expected, result)
	// 	}
	// }
	t.Log(
		nextGreaterElement(123),
		nextGreaterElement(100),
		nextGreaterElement(321),
		nextGreaterElement(6),
		nextGreaterElement(1246553),
	)
}
