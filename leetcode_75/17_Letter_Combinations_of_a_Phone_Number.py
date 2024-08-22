class Solution(object):
    # def digit2letter(self, digit):
    #     if digit == 2:
    #         return ["a", "b", "c"]
    #     if digit == 3:
    #         return ["d", "e", "f"]
    #     if digit == 4:
    #         return "ghi"
    #     if digit == 5:
    #         return "jkl"
    #     if digit == 6:
    #         return "mno"
    #     if digit == 7:
    #         return "pqrs"
    #     if digit == 8:
    #         return "tuv"
    #     if digit == 9:
    #         return "wxyz"

    # def sol(self, digits, m, pos):
    #     if pos>=m:
    #         return ''
    #     else:
    #         result = []
    #         letters = self.digit2letter(int(digits[pos]))
    #         for letter in letters:
    #             result.append(letter + self.sol(digits, m, pos+1))
    #         return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numCharMapper = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r', 's'],
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z']
        }
        res = []
        for digit in digits:
            if not res:
                res = numCharMapper[digit]
            else:
                temp = numCharMapper[digit]
                tempRes = []
                for charI in res:
                    for charJ in temp:
                        tempRes.append(charI + charJ)
                
                res = tempRes
        return res
        
        