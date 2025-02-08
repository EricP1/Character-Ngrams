
# Function to extract every character ngrams
# out of all word-forms in a text segment (named s)

import re

def EveryCharNgrams(s):
     WordForms = s.split(" ")
     SubStringList = []
     for word in WordForms:
             for i in range(len(word)):
                     for j in range(i+1, len(word)+1):
                             SubStringList.append(word[i:j])
     return SubStringList


text = "Enter your sentence or paragrph here"

# Convert non-alphanumeric charcters to spaces
text = re.sub(r'[^\w+( +\w+)*$]', ' ', text)
print ("My text without non-alphanumeric characters with spaces:", text)

# Every character ngrams extraction from my text

MyNgrams = EveryCharNgrams(text)

print ("Number of ngrams extracted and my ngrams extracted from my text:", len(MyNgrams), MyNgrams)

