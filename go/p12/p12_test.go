package p12

import (
	"testing"
)

type testCase struct {
}

var (
	testCases = []testCase{}
)

func TestAll(t *testing.T) {
	t.Log(intToRoman(3))
	t.Log(intToRoman(4))
	t.Log(intToRoman(9))
	t.Log(intToRoman(58))
	t.Log(intToRoman(1994))
	t.Log(intToRoman(3999))
}
