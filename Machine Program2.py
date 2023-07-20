#1. Ask the user to enter a plain message.
#2. Encrypt the message.
#3. Display the encrypted message.

#Enter a Message: Hello World
#Encrypted Message: ehoorqtruog
text = input("Enter Text: ")
class Solution:
    def solve(self, s, k):
        def shift(c):
            i = ord(c) - ord('a')
            i += k
            i %= 26
            return chr(ord('a') + i)

        return "".join(map(shift, s))


ob = Solution()
input(ob.solve(text, 3))


