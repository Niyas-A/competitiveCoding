class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not s or not words:
            return res

        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)
        
        # print(word_freq)
        n = len(s)
        word_len = len(words[0])
        subString_len = len(words)*word_len
        for i in range(n-subString_len+1):
            subString_map = {}
            j = i
            while j < i+subString_len:
                cur_word = s[j:j+word_len]

                if cur_word not in word_freq:
                    break

                subString_map[cur_word] = 1 + subString_map.get(cur_word,0)

                if subString_map[cur_word] > word_freq[cur_word]:
                    break
                # print(j,j+word_len,s[j:j+word_len])
                # if word_freq.get(s[j:j+word_len],0) - subString_map.get(s[j:j+word_len],0) > 0:
                #     subString_map[s[j:j+word_len]] = 1 + subString_map.get(s[j:j+word_len],0)
                # else:
                #     break
                j += word_len
            if j == i+subString_len:
                res.append(i)
            # print(i, subString_map)
            # if subString_map == word_freq:
            #     res.append(i)
        return res
        