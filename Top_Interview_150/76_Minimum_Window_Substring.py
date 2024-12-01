class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # res = []
        result = ''
        t_freq = {}
        for char in t:
            t_freq[char] = 1 + t_freq.get(char,0)
        s_freq = {}
        need = len(t_freq)
        have = 0
        l = 0
        r = -1
        n = len(s)
        min_len = n+1 
        while r<n:
            print(l,r)
            while r<n-1 and need != have:
                r += 1
                char = s[r]
                if char in t_freq:
                    s_freq[char] = 1 + s_freq.get(char,0)
                    if s_freq[char] == t_freq[char]:
                        have += 1
            if need != have:
                break
            while need == have:
                if min_len > r-l+1:
                    min_len = r-l+1
                    result = s[l:r+1] 
                # res.append(s[l:r+1])
                char = s[l]
                if char in s_freq:
                        if s_freq[char] == t_freq[char]:
                            have -= 1
                        s_freq[char] = s_freq[char] - 1
                l += 1
        # print(res)
        return result