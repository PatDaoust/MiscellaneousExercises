# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:33:16 2022

@author: catal
"""

import re

"""exercises from
https://holypython.com/advanced-python-exercises/project-regular-expressions-regex/
solutions by Pat Daoust"""

"""exercise 6-a
From the list keep only the lines that start with a number or a letter after > sign.
"""


str="""
>Venues
>Marketing
>medalists
>Controversies
>Paralympics
>snowboarding
>[1]
>Netherlands
>[2]
>Norway
>[10]
>[11]
>References
>edit
>[12]
>Norway
>Germany
>Canada
>Netherlands
>Japan
>Italy
>Belarus
>China
>Slovakia
<$#%#$%
<#$#$$
<**&&^^
>Slovenia
>Belgium
>Spain
>Kazakhstan
>[15]
>1964
>1968
>1972
>1992
>1996
>2000"""


data = re.findall('>\w+', str)
# print(data)


"""Exercise 6-b
Write a regex so that the full email addresses are extracted.
i.e.: mike@protonmail.com"""


str2 = 'The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'

regex = "\w+@\w+.com"
emails = re.findall(regex, str2)

# print(emails)


"""Exercise 6-c
This time write a regex to get only the part of the email before the "@" sign
and include the "@" sign.
i.e: only mike@ part from mike@protonmail.com
"""

regex2 = "\w+@"
emails2 = re.findall(regex2, str2)
# print(emails2)


"""Exercise 6-d
This time write a regex to get only the part of the email before the "@" sign
excluding the "@" sign.
i.e: only mike part from mike@protonmail.com
"""

regex3 = "(\w+)@"
emails3 = re.findall(regex3, str2)
# print(emails3)


"""Exercise 6-e
Find the words with exactly 8 letters using regex"""

str3 = '''Au pays parfume que le soleil caresse,
J'ai connu, sous un dais d'arbres tout empourpres
Et de palmiers d'ou pleut sur les yeux la paresse,
Une dame creole aux charmes ignores.'''

regex4 = "\w{8}"
words8 = re.findall(regex4, str3)
# print(words8)
