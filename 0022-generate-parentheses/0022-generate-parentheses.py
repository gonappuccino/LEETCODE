class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s: str, open_count: int, close_count: int):
            # 종료 조건: 괄호 길이가 2n이면 완성
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # 여는 괄호 추가 (n개까지만 가능)
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            # 닫는 괄호 추가 (닫는 수가 여는 수보다 작을 때만 가능)
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
            