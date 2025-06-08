"""
Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)

link: https://www.youtube.com/watch?v=K8L6KVGG-7o

cheatsheet:

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

These anchors match invisible chars before or after chars

\b      - Word Boundary (= whitespace or non-alphanumeric char)
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in 

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

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

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
 
"""