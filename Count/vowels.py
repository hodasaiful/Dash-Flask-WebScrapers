def count(sentence:str):
    word = sentence.lower()
    vowels ="aeiou"
    vow = []
    isvowel = 0
    cons = []
    isconsonant =0
    for x in word:
        if ord(x) > 64 and ord(x) < 123  and ord(x) not in (91,92,93,94,95,96):
            if x in vowels:
                isvowel = isvowel+1
            else:
                isconsonant = isconsonant+1
        else:
            pass
    return  'Count of consonants is -->  ', isconsonant, 'Count of vowels is -->  ', isvowel
   
    
