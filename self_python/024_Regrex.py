import re
# resource: https://www.youtube.com/watch?v=K8L6KVGG-7o

"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

Anchors:
\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
901--555-*1234
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

sentence = 'Start a sentence and then bring it to an end'

# re.compile = specify patterns to be search
pattern = re.compile(r'start', re.I)
# pattern = re.compile(r'\.', re.I) : search for a dot

# pattern.search: look for the pattern in the given input string
matches = pattern.search(sentence)

print(matches)  # <re.Match object; span=(0, 5), match='Start'>
# print(pattern.match(sentence))  # <re.Match object; span=(0, 5), match='Start'>

# Anchors: >>>>>>>>>>>>>>>>>>>>>>>>>>
# \b or \B >>>>>>>>>>>>>>>>>>>>>>>>>>
# input has `Ha HaHa`
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)

for match in matches:
    # <re.Match object; span=(66, 68), match='Ha'>
    # <re.Match object; span=(69, 71), match='Ha'>
    print(match)

pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)

for match in matches:
    # `Ha Ha[Ha]`
    # <re.Match object; span=(71, 73), match='Ha'>
    print(match)

# ^: begin or $: end >>>>>>>>>>>>>>>>>>>>>>>>>>
# begin
pattern = re.compile(r'^Start')
# Start MUST be at the beginning of the string
# re.compile(r'^a') will not return anything bc its not at the beginning of the string
matches = pattern.finditer(sentence)

for match in matches:
    # <re.Match object; span=(0, 5), match='Start'>
    print(match)

# -- end of string
pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)

for match in matches:
    # <re.Match object; span=(41, 44), match='end'>
    print(match)

# -- match phone number in text_to_search
"""
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
901--555-*1234 --->careful!!!!
"""
# \d to match any digit --> need first 3 digit: \d\d\d
# use . to match any pattern: 123[.] or 123[*] ==> \d\d\d.\d\d\d.\d\d\d
# NOTE: if we wanna match ONLY "-" or "." then use: \d\d\d[-.]\d\d\d[-.]\d\d\d
# 901--555-*1234 --->careful!!!! ==> ?????
# what about we only want start with either 8 or 9 follow by 00: [89]00[-.]\d\d\d[-.]\d\d\d
# matching digit between 1-5: [1-5]
# matching char between a-z and A-Z: [a-zA-Z]
# IMPORTANT AS FUCK:
# - ^ outside [] := beginning of the string
# ^ inside [] := negation; ex: [^a-z] = amtching anything that is NOT a-z

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    # <re.Match object; span=(151, 162), match='321-555-432'>
    # <re.Match object; span=(164, 175), match='123.555.123'>
    # <re.Match object; span=(177, 188), match='123*555*123'>
    # <re.Match object; span=(190, 201), match='800-555-123'>
    # <re.Match object; span=(203, 214), match='900-555-123'>
    print(match)

"""
cat
mat
pat
bat

==> we want everything that end with [at] but DOES NOT START WITH [b]
pattern = re.compile(r'[^b]at')
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# So far we only match 1 single char at a time ==> ez to make mistake
# USE QUANTIFIER TO MATCH MULTIPLE CHAR AT A TIME
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""
Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
"""

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d') now becomes using exact number match
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    # <re.Match object; span=(151, 162), match='321-555-432'>
    # <re.Match object; span=(164, 175), match='123.555.123'>
    # <re.Match object; span=(177, 188), match='123*555*123'>
    # <re.Match object; span=(190, 201), match='800-555-123'>
    # <re.Match object; span=(203, 214), match='900-555-123'>
    print(match)

"""
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

--> take out all the name with mr
"""
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# Mr\.: Mr follows by "."
# "?" ensures that the "\." is optional
# \s: space
# next follows by a capital letter [A-Z]
# follows by a word character with quantity at least 1 words: \w*

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# VERY IMPORTANT: using `GROUP: (|:or &:and) to find all the Mr Ms Mrs

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# >>>>>>>>>>>>>>>>>>>>>>>
# Matching emails
# >>>>>>>>>>>>>>>>>>>>>>>

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# match at least 1 or more characters from a-Z0-9 until we hit the "@" symbol: [a-zA-Z0-9]+@
# [a-zA-Z0-9[_.+-]][+]: allow to have "_.+-" in the email name hieu_nguyen.quoc [+] allows at least 1 of the matching

matches = pattern.finditer(emails)

for match in matches:
    print(match)


# >>>>>>>>>>>>>>>>>>>>>>>
# Matching domain names using groups
# >>>>>>>>>>>>>>>>>>>>>>>
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)

#
for match in matches:
    # https://www.google.com
    # http://coreyms.com
    # https://youtube.com
    # https://www.nasa.gov
    print(match.group(0))  # group 0 is the entire match

# we only want 2nd and 3rd group
# note that group 0 is the entire match
# now we wanna replace the urls by the 2nd and 3rd groups: domain anme and top level domain
subbed_urls = pattern.sub(r'\2\3', urls)


print(subbed_urls)
"""
google.com
coreyms.com
youtube.com
nasa.gov
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# OTHER METHODS OTHER THAN `finditer()`

#[('www.', 'google', '.com'), ('', 'coreyms', '.com'), ('', 'youtube', '.com'), ('www.', 'nasa', '.gov')]
print(pattern.findall(urls))

# pattern.search: can be use to match anything in the string regardless of locations

# pattern.match: only output result if the match occurs at the beginning of the string
