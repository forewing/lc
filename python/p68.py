class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        todo = []
        todo_size = 0

        def combine(todo, todo_size):
            spaces = maxWidth - todo_size

            if len(todo) == 1:
                return todo[0] + " " * spaces

            base = " " * (spaces // (len(todo) - 1))
            first = spaces % (len(todo) - 1)
            result = []
            for i in range(len(todo) - 1):
                result.append(todo[i])
                result.append(base)
                if i < first:
                    result.append(" ")
            result.append(todo[-1])
            return "".join(result)

        for word in words:
            lw = len(word)
            if todo_size + len(todo) + lw > maxWidth:
                ans.append(combine(todo, todo_size))
                todo = []
                todo_size = 0
            todo.append(word)
            todo_size += lw

        final = " ".join(todo) + " " * (maxWidth - len(todo) + 1 - todo_size)
        ans.append(final)
        return ans
