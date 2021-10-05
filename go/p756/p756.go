package p756

/*
 * @lc app=leetcode.cn id=756 lang=golang
 *
 * [756] 金字塔转换矩阵
 */

// @lc code=start

var (
	charset = []string{
		"A", "B", "C", "D", "E", "F", "G",
	}
	allowedTable  map[string]string
	allowedBottom map[string]bool
)

func initAllowed(allowed []string) {
	allowedTable = make(map[string]string)
	allowedBottom = make(map[string]bool)

	for _, allow := range allowed {
		prefix := allow[0:2]
		if _, ok := allowedTable[prefix]; !ok {
			allowedTable[prefix] = ""
		}
		allowedTable[prefix] += allow[2:3]
		allowedBottom[prefix] = true
	}

	for _, c := range charset {
		allowedBottom[c] = true
	}

	// fmt.Println(allowedTable)
	// fmt.Println(allowedBottom)
}

func solvePyramidTransition(bottom string, exist string) (isAllowed bool) {
	// new case
	if len(exist) == 0 {
		if _, ok := allowedBottom[bottom]; ok {
			return true
		}

		if len(bottom) == 2 {
			return false
		}

		defer func() {
			if isAllowed {
				allowedBottom[bottom] = true
			}
		}()
	}

	// compeleted case
	if len(bottom) < 2 {
		return solvePyramidTransition(exist, "")
	}

	// todo case
	avaliable, ok := allowedTable[bottom[0:2]]
	if !ok {
		return false
	}

	for _, c := range avaliable {
		if len(exist) > 0 {
			if _, ok := allowedBottom[exist[len(exist)-1:]+string(c)]; !ok {
				continue
			}
		}
		if solvePyramidTransition(bottom[1:], exist+string(c)) {
			return true
		}
	}

	return false
}

func pyramidTransition(bottom string, allowed []string) bool {
	initAllowed(allowed)
	return solvePyramidTransition(bottom, "")
}

// @lc code=end
