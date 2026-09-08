class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s

        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            word_length = int(s[i:j])
            word = s[j+1 : j + word_length + 1]
            decoded.append(word)
            i = word_length + j + 1

        return decoded