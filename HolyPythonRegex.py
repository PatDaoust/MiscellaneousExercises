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


"""Exercise 6-f
Find the numbers starting with 212."""

str4 = '''Ancient Script 21299: The Takenouchi documents are the ancient historical records that have been secretly preserved and passed down from generation to generation by the Takenouchi family, the head of family being the chief priest of the Koso Kotai Jingu shrine. 212-111-5932 '''

regex5 = "212[-*\d*]*"
data2 = re.findall(regex5, str4)
# print(data2)


"""Exercise 6-g
You are given stock prices for related financial tickers.
(Symbols representing companies in the stock market)

Find a way to extract the tickers mentioned in the report.
i.e.: TSLA, NFLX ...
"""

str5 = """Some of the prices were as following TSLA:749.50, ORCL: 50.50, GE: 10.90, MSFT: 170.50, BIDU: 121.40. As the macroeconomic developments continue we will update the prices. """


regex6 = "([A-Z]+):"
data3 = re.findall(regex6, str5)
# print(data3)


"""Exercise 6-h
Find the html tags that are more than 4 letters.
Html tags can be found inside <> characters and closing html tags can be found
in the same format after / character. </>
i.e.: <param> </param>
"""


str6 = """<div class="tut-list tut-list-new tut-row ">
<div class="tut-list-primary"> <div class="tut-vote">
<video>intro</video>
<span class="count">50</span><span class="tut-upvotes-text hidden">Upvotes</span></a></div>
<center>k="11" rel="nofollow"></center>
<span class="tutorial-title-txt">Automate the Boring Stuff with Python</span>
<span class="tut-title-link">  <span class="js-tutorial" data-id="3529"
title="Automate the Boring Stuff with Python" target="_blank">(udemy.com)</span
</span>  </a></div> <div class="action-footer">
<form class="save-tutorial-form" method="post" <button></button> </form>"""


regex7 = "<(\w+)>"
data4 = re.findall(regex7, str6)
# print(data4)


"""Exercise 6-i
Loop through the list and apply regex to each element so that only items ending with
semicolon (;) are matched."""


list1 = ["js/prettify-full.en.js 4e6ee9163220",
         "js/moderator.en.js:",
         "transaction no: 75553942;",
         "",
         "transaction no: 75551263;",
         "transaction no: 46553942;",
         "c01c47765ca21b82b08b90403b4c7af3886098683e3869ad1:",
         "transaction no: 75554942;"]

regex8 = ";$"
lst = []
for elem in list1:
    result = re.search(regex8, elem)
    if result:
        lst.append(elem[:-1])
# print(lst)
