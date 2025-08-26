class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        cnt_board = Counter(ch for row in board for ch in row)
        cnt_word = Counter(word)
        for ch, need in cnt_word.items():
            if cnt_board[ch] < need:
                return False

        def dfs(r, c, k):
            # 마지막 글자 도달
            if k == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
                return False

            tmp = board[r][c]
            board[r][c] = '#'

            found =(
                dfs(r+1, c, k+1) or
                dfs(r-1, c, k+1) or
                dfs(r, c+1, k+1) or
                dfs(r, c-1, k+1)
            )
            board[r][c] = tmp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
            
        
        
        