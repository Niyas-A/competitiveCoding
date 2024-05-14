class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        d1 = {}
        for i,c in enumerate(word1):
            if c in d1.keys():
                d1[c].append(i)
            else:
                d1[c] = [i]
        # l1 = sorted(list(d1.values()))
        l1 = sorted([len(l) for l in list(d1.values())])
        # print(l1)
        # print(sorted([len(l) for l in l1])) 
        d2 = {}
        for i,c in enumerate(word2):
            if c in d2.keys():
                d2[c].append(i)
            else:
                d2[c] = [i]
        # l2 = sorted(list(d2.values()))
        l2 = sorted([len(l) for l in list(d2.values())])
        # print(l2)
        # print(sorted([len(l) for l in l2])) 
        # if l1 == l2:
        # print(d1.keys())
        # print(d2.keys())
        # print(sorted(d1.keys()) == sorted(d2.keys()))
        # if sorted([len(l) for l in l1]) == sorted([len(l) for l in l2]) and sorted(d1.keys()) == sorted(d2.keys()):
        if l1 == l2 and sorted(d1.keys()) == sorted(d2.keys()):
            return True
        else:
            return False