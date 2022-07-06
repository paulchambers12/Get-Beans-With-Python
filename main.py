#credits and shit go here
#Bluescreen and Antie 

#includes go here
from collections import Counter
import math
import os
import random
import requests
import sys
from urllib.request import urlopen
import re

#methods get initialized here
def swap_case(s):
    thing = ("".join(c.upper() if c.islower() else c.lower() for c in s))
    return thing

#main method
if __name__ == '__main__':
    #s = raw_input()
    #result = swap_case(s)
    #print result

    # html_content = urlopen('https://www.tesco.ie/groceries/en-IE/search?query=beans%27).read().decode(%27utf-8%27)
    html_content = urlopen('https://www.tesco.ie/groceries/zone/contact-us/%27).read().decode(%27utf-8%27')
    #print(html_content)
    print("This is html_content: {0}".format(html_content))
    print("This is beans: {0}".format('beans'))
    beans = '[w.-]+@[w.-]+'
    matches = re.findall('beans', html_content, flags=0);

    if len(matches) == 0:
        print('This website has no beans to sell')
    else:
        print(matches)
