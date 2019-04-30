class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversedSentence = ""
        for word in words:
            reversedWord = "".join(list(reversed(word)))


            reversedSentence = reversedSentence + reversedWord + " "
        r = reversedSentence.strip()
        return r

