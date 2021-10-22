package p12

/*
 * @lc app=leetcode id=12 lang=golang
 */

// @lc code=start

var (
	transform = [][]string{
		{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
		{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
		{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
		{"", "M", "MM", "MMM", "", "", "", "", "", ""},
	}
)

func intToRoman(num int) string {
	if num < 1 || num > 3999 {
		panic("out of range")
	}

	result := ""

	for i := 0; i < 4 && num > 0; i++ {
		result = transform[i][num%10] + result
		num /= 10
	}

	return result
}

// @lc code=end
