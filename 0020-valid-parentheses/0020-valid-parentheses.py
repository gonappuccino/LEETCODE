class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False
        

        for brackets in s:
            if brackets == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif brackets == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif brackets == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(brackets)
        return True if len(stack) == 0 else False

               