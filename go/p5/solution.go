package p5

func longestPalindrome(s string) string {
	n := len(s)

	l, r := 0, n
	al, ar := 0, 1

	for l < r {
		if r-l > ar-al {
			tl, tr := l, r
			ok := true
			for tl < tr {
				if s[tl] == s[tr-1] {
					tl++
					tr--
				} else {
					ok = false
					break
				}
			}
			if ok {
				al, ar = l, r
			}
		}
		r--
		if l == r {
			l++
			r = n
		}
	}

	return s[al:ar]
}
