class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        s = []
        prev_char = chars[0]
        count = 1
        for i in range(n-1):
            if chars[i+1] == prev_char:
                count += 1
            else:
                if count > 1:
                    s.append(prev_char)
                    [s.append(str(k)) for k in str(count)]
                    # s.append(str(count))
                    count = 1
                    prev_char = chars[i+1]
                else:
                    s.append(prev_char)
                    count = 1
                    prev_char = chars[i+1]
        if count > 1:
            s.append(prev_char)
            [s.append(str(k)) for k in str(count)]
            # s.append(str(count))
        else:
            s.append(prev_char)
        # print(s)
        chars[0:len(s)] = s
        return len(s)
        