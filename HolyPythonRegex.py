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

print(data)
