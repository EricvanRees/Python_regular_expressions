"""
Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)

link: https://www.youtube.com/watch?v=K8L6KVGG-7o

cheatsheet:

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Any char which is NOT a digital digit
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

These anchors match invisible chars before or after chars

\b      - Word Boundary (= whitespace or non-alphanumeric char)
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
()      - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

"""



#import re module
import re

text_to_search = '''
acdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

# 1. finding matches

sentence = 'Start a sentence and then bring it to an end'

# a raw string is any string prefixed with an 'r'
# this tells Python not to handle any backslashes in a special way:

print('\tTab') # prints Tab
print(r't\Tab') # prints t\Tab

# use the re.compile method to specify patterns to search for using variables for reuse

pattern = re.compile(r'abc')

# finditer returns iterator that contains all matches
matches = pattern.finditer(text_to_search)

# prints <_sre.SRE_Match object: span=(1, 4), match='abc'>
# span is the beginning and end index of match
# this enables you to use string slicing to print out only the match

for match in matches:
  print(match)
  
# search for special character such as a dot (.) with escape char (\):

pattern =  re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
  print(match)

"""
# 2. pattern matching: 

Examples of special chars from cheatsheet above:

matches all chars except newline:
pattern = re.compile(r'.') 

matches all digits:
pattern = re.compile(r'\d')

matches all non-digits:
pattern = re.compile(r'\D')

matches all word chars:
pattern = re.compile(r'\w')

matches non-word chars:
pattern = re.compile(r'\W')

matches tabs, spaces, newlines:
pattern = re.compile(r'\s')

matches non-tabs, spaces, or newlines:
pattern = re.compile(r'\S')

does NOT match the 3rd "Ha" as there is no word boundary before it:
pattern = re.compile(r'\bHa')  

Does ONLY match the 3rd "Ha":
pattern = re.compile(r'\BHa') 

Matches "Start" at beginning of string:
pattern = re.compile(r'^Start') 

matches = pattern.finditer(sentence)
Matches "end" at end of string:

pattern = re.compile(r'end$') 
matches = pattern.finditer(sentence)

match both phone numbers above using ANY separator:
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 

find all phone numbers from text file:

with open('data.text', 'r', encoding='utf-8') as f:
  contents = f.read()
  
  matches = pattern.finditer(contents)
  
  for match in matches:
    print(match)
    
"""

# 3 Character sets use square brackets (=[]) to find a match

# find a dash or a dot
 
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# you do not need to escape a dot or dash inside a character set as they have slightly different rules

# a character set to match only 800 and 900 numbers:
# first char set looks for 8 or 9 at the beginning, followed by two literal zeros:

pattern = re.compile(r'[89][00][-.]\d\d\d[-.]\d\d\d\d')

# match digits within a specified range, using a dash:
pattern = re.compile(r'[1-5]')

# this works for letters as well:
pattern = re.compile(r'[a-z]')
pattern = re.compile(r'[a-zA-Z]')

# within a character string, a carrot sign (^) negates the set and matches everything that is not in that character set.

# carrot sign will match everything that is NOT uppercase or lowercase letter

pattern = re.compile(r'[^a-zA-Z]')

# match everything that is not a "b" and ends with "at": cat, mat, pat, but NOT bat

pattern = re.compile(r'[^b]at')

# 4 use quantifiers to match more than one character at once

# example without quantifiers:
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# same exmample with quantifiers:
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# match names with Mr., Mr, etc.
# use question mark for optional chars
# so here the period is optional:
# * = matches zero or more word chars
 
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# 5 Groups - using () - allow to match for several different patterns 

# match for Mrs. and Ms
pattern = re.compile(r'Mr(r|s|rs)\.?\s[A-Z]\w*')
# same thing but more readable:
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

'''
Exercise: write a regex that matches all these emails:

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

1st email address:
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')

2nd email address:
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)') 

3rd email address:
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') 
'''


