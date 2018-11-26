class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None:
            return words
        english_alphabet_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # for Each word find out the integer value for it. In Java it would be
        # char -'a' (Find out the equivalent in python)
        # For each char find the morse code and add it to a Set

        #Step 1
        pattern_set = set()
        for word in words:
            pattern = ''
            for ch in list(word):
                int_value = ord(ch) - 97
                pattern += english_alphabet_code[int_value]
            pattern_set.add(pattern)
        return len(pattern_set)


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))