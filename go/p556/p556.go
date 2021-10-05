package p556

import (
	"math"
	"sort"
)

/*
 * @lc app=leetcode id=556 lang=golang
 */

// @lc code=start

func nextGreaterElement(n int) int {
	length, digits := split(n)

	for i := 1; i < length; i++ {
		p := -1
		for j := 0; j < i; j++ {
			if digits[j] > digits[i] && (p == -1 || digits[j] < digits[p]) {
				p = j
			}
		}
		if p != -1 {
			digits[i], digits[p] = digits[p], digits[i]
			sort.Slice(digits[0:i], func(i int, j int) bool {
				return digits[i] > digits[j]
			})
			return combine(digits)
		}
	}

	return -1
}

func split(n int) (length int, digits []int) {
	length = 0
	digits = []int{}
	for t := n; t > 0; t /= 10 {
		length++
		digits = append(digits, t%10)
	}
	return
}

func combine(digits []int) int {
	var result int64
	for i := len(digits) - 1; i >= 0; i-- {
		result *= 10
		result += int64(digits[i])
	}
	if result > math.MaxInt32 {
		return -1
	}
	return int(result)
}

// @lc code=end
