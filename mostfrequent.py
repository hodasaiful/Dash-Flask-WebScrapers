'''
The file bbc.txt (scraped from the web can be found at -- >https://drive.google.com/file/d/1w6HJeaVhTIFvimV1O35YvJipTSMtDDbZ/view?usp=sharing
'''


filter =['in','to','of','for','the','if','by','gap','after','and','return','showed','four','at','it','only','face','clear',
        'how','app','a']
dict={}
fhand = open('C:\\PYTHON\\PYTHONCODE\\bbc.txt')
for line in fhand:
    line = line.rstrip()
    line = line.lower()
    words =line.split()
    for i in words:
        if i in filter:
            pass
        elif i not in dict:
            dict[i] = 1      
        else:
            dict[i] = dict[i]+1
import pandas as pd
S = pd.Series(dict)
S.sort_values(ascending=False, inplace=True)
print(S)
#S.head(10).plot(kind='bar', color ='blue', alpha=0.7, figsize=(8,4), rot=75);