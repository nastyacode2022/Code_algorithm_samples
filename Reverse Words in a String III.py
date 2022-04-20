"""
Given a string s,
reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ''
        count = 0
        count2 = 0
        for zopa in s:
            if zopa == ' ':
                count += 1
            else:
                count2 += 1
        if not count2 == len(s):
            for letter in range(len(s)):
                if s[letter] == ' ':
                    for i in range(letter):
                        if s[letter - 1 - i] != ' ':
                            new_str += s[letter - 1 - i]
                        else:
                            break
                    if not len(new_str) == len(s):
                        new_str += ' '
                        count -= 1
                elif count == 0:
                    for j in range(len(s)):
                        if s[len(s) - 1 - j] != ' ':
                            new_str += s[len(s) - 1 - j]
                        else:
                            return new_str
        else:
            return s[::-1]