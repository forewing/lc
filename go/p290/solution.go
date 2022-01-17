package main

import "strings"

func wordPattern(pattern string, s string) bool {
	n := len(pattern)
	ss := strings.Split(s, " ")
	if n != len(ss) {
		return false
	}

	pat2word := make([]string, 26)
	exist := make(map[string]bool)
	for i := range pattern {
		pati := pattern[i] - 'a'
		if len(pat2word[pati]) != 0 {
			if pat2word[pati] != ss[i] {
				return false
			}
			continue
		}
		if _, ok := exist[ss[i]]; ok {
			return false
		}
		pat2word[pati] = ss[i]
		exist[ss[i]] = true
	}

	return true
}

func main() {
	wordPattern("abba", "dog cat cat fish")
}
