package p1178

type puzzleIndex struct {
	puzzle int
	index  int
}

func str2int(str string) (result, cnt int) {
	for _, c := range str {
		t := 1 << (c - 'a')
		if result&t == 0 {
			cnt++
		}
		result |= t
	}
	return result, cnt
}

func findNumOfValidWords(words []string, puzzles []string) []int {
	wordsi := []int{}
	for _, word := range words {
		result, cnt := str2int(word)
		if cnt <= 7 {
			wordsi = append(wordsi, result)
		}
	}
	puzzlesi := map[rune][]puzzleIndex{}
	for i, puzzle := range puzzles {
		result, _ := str2int(puzzle)
		puzzlesi[rune(puzzle[0])] = append(puzzlesi[rune(puzzle[0])], puzzleIndex{result, i})
	}

	result := make([]int, len(puzzles))

	for _, wordi := range wordsi {
		for tmp, i := wordi, 'a'; tmp > 0; tmp, i = tmp>>1, i+1 {
			if tmp&1 == 1 {
				for _, p := range puzzlesi[i] {
					if wordi|p.puzzle == p.puzzle {
						result[p.index]++
					}
				}
			}
		}
	}

	return result
}
