package p503

/*
 * @lc app=leetcode.cn id=503 lang=golang
 *
 * [503] 下一个更大元素 II
 */

// @lc code=start
type element struct {
	index int
	value int
}

type stack struct {
	head     int
	elements []element
}

func newStack(n int) *stack {
	return &stack{
		head:     0,
		elements: make([]element, n),
	}
}

func (s *stack) empty() bool {
	return s.head == 0
}

func (s *stack) push(index int, value int) bool {
	if s.head >= cap(s.elements) {
		return false
	}
	s.elements[s.head] = element{
		index: index,
		value: value,
	}
	s.head++
	return true
}

func (s *stack) pop() {
	if !s.empty() {
		s.head--
	}
}

func (s *stack) peak() (index int, value int) {
	if s.empty() {
		return -1, -1
	}
	return s.elements[s.head-1].index, s.elements[s.head-1].value
}

func nextGreaterElements(nums []int) []int {
	n := len(nums)
	result := make([]int, n)
	done := make([]bool, n)
	s := newStack(n * 2)

	for i := 0; i < n*2; i++ {
		index := i % n
		value := nums[index]

		for !s.empty() {
			ei, ev := s.peak()
			if value <= ev {
				break
			}
			result[ei] = value
			done[ei] = true
			s.pop()
		}
		s.push(index, value)
	}

	for !s.empty() {
		ei, _ := s.peak()
		if !done[ei] {
			result[ei] = -1
		}
		s.pop()
	}

	return result
}

// @lc code=end
