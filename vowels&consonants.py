'''
Prompt user for a sentence- filter out special characters, blank spaces etc
and return the number of vowels and consonants in it
'''

word = list(input("Enter the word: ").lower())
vowels =['a','e','i','o','u']
isvowel = 0
isconsonant =0
#ascii 65 -90 (A-Z)
#ascii - 97-122 (a-z)
for x in word:
    if ord(x) > 64 and ord(x) < 123  and ord(x) not in (91,92,93,94,95,96):
        if x in vowels:
            isvowel = isvowel+1
        else:
            isconsonant = isconsonant+1
    else:
        pass
print("The number of consonants is",isconsonant, "The number of vowels is",isvowel)