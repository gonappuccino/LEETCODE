class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # 정수 나눗셈, 0을 기준으로 자르기 (Python에서 조심)
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]