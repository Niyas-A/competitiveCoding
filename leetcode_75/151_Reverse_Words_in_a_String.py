class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ''
        n = len(s)
        right = n-1
        left = n-1
        for i in range(n):
            # print(s[n-i-1])
            if s[n-i-1] == ' ' and s[right] != ' ':
                left = n-i
                # print(s[left:right+1])
                r += (s[left:right+1])
                r += ' '
                right = n-i-1
            if s[n-i-1] != ' ' and s[right] == ' ':
                right = n-i-1
            if i == n-1 and s[right] != ' ':
                left = 0
                print(s[left:right+1])
                r += (s[left:right+1])
                # r += ' '
                right = n-i-1
        if r[-1] == ' ':
            r = r[0:-1]
        # print(r)
        return r
            