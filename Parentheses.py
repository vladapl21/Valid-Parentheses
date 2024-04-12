class Solution(object):
  def isValid(self, s):
      """
      :type s: str
      :rtype: bool
      """
      stack = []
      d = {')':'(', '}':'{', ']':'['}

      for i in range(len(s)):
          if s[i] in ['(', '{', '[']:
              stack.append(s[i])
          else:
              if len(stack) == 0 or d[s[i]] != stack[-1]:
                  return False
              else:
                  stack.pop(-1)

      return len(stack) == 0