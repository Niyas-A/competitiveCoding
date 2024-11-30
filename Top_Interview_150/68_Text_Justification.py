def ceildiv(a, b):
    return -(a // -b)

class Solution(object):
    def words2width(self, count, length, temp, maxWidth):
        res = ''
        spaces = maxWidth - length
        if count == 1:
            res = temp[0] + ' '*(maxWidth-length)
        else:
            i = 0
            while i<count:
                if i<count-1:
                    sp = ceildiv(spaces,(count-i-1))
                    spaces -= sp
                    res += temp[i] + ' '*(sp)
                else:
                    res += temp[i]
                i += 1
        return res

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        temp = []
        count = 0
        length = 0
        res = []
        n = len(words)
        for i in range(n+1):
            if i<n and length + len(words[i]) + count <= maxWidth:
                temp.append(words[i])
                length += len(words[i])  
                count += 1
            else:
                if i == n:
                    text = ' '.join(temp) + ' ' * (maxWidth-length-count+1)
                else:
                    text = self.words2width(count, length, temp, maxWidth)
                res.append(text)
                if i < n:
                    length = len(words[i])
                    count = 1
                    temp = []
                    temp.append(words[i])
        return res
