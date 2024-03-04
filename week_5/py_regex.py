# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
from row import txt

x = re.search("ab*", txt) #ab* - * используется для 
print(x)


# Write a Python program that matches a string that
# has an 'a' followed by two to three 'b'.

import re
from row import txt

x = re.search("a(b{2}b?)", txt)

print(x)



# Write a Python program to find sequences
# of lowercase letters joined with a underscore.

import re
from row import txt

x = re.findall("[a-z]+_[a-z]+", txt)

print(x)



# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
from row import txt

x = re.findall("[A-Z][a-z]+", txt)
print(x)



# Write a Python program that matches a string that has an
# 'a' followed by anything, ending in 'b'.

import re
from row import txt

x = re.findall("a.*b$", txt)
print(x)



# Write a Python program to replace all occurrences of space,
# comma, or dot with a colon.

import re
from row import txt

x = re.sub("[.,\s]", ":", txt)
print(x)


# Write a python program to convert snake case string to camel case string.

import re

def convertor(match):
    return match.group(0)[1].upper()

txt = "snake_case_base_bibibibibi"
x = re.sub(r'_.', convertor, txt)

print(x)



# Write a Python program to split a string at uppercase letters.
import re

stringi = "SplitThisStringAtUpperCase"
x = re.findall('[A-Z][^A-Z]*', stringi)
print(x)



# Write a Python program to insert spaces between words starting with capital letters.
import re

stringi = "ThisIsAStringWithCapitalWords"
x = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', stringi)

while(x != re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', x)):
    x = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', x)

print(x)


# Write a Python program to convert a given camel case string to snake case.
import re

s = "camelCaseStringExample"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(x)