"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Input: x = 123
Output: 321
"""

class Solution:

    def range(self, integer):

        if integer in range(-2147483648, 2147483648):
            return str(integer)
        else:
            return 0

    def reverse(self, x: int) -> int:

        new_str = str(x)
        if len(new_str) == 1:
            return new_str
        elif new_str[0] == '-' and new_str[-1] == '0':
            count = 0
            for i in range(len(new_str.replace(new_str[0], ''))):
                if new_str.replace(new_str[0], '')[::-1][i] == '0':
                    count += 1
                else:
                    return Solution.range(self, int('-' + new_str.replace(new_str[0], '')[::-1][count:]))

        elif new_str[-1] == '0':
            count = 0
            for i in range(len(new_str)):
                if new_str[::-1][i] == '0':
                    count += 1
                else:
                    return Solution.range(self, int(new_str[::-1][count:]))

        elif new_str[0] == '-':
            return Solution.range(self, int('-' + new_str.replace('-', '')[::-1]))
        else:
            return Solution.range(self, int(new_str[::-1]))