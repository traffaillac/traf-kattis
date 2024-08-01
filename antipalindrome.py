from string import *

S = ''.join(c.lower() for c in input() if c in ascii_letters)
print("Palindrome" if any(S[i:j]==S[i:j][::-1] for i in range(len(S)-1) for j in range(i+2,len(S)+1)) else "Anti-palindrome")