#credits and shit go here
#Bluescreen and Antie 

#includes go here
from collections import Counter


#methods get initiallized here
def swap_case(s):
    thing = ("".join(c.upper() if c.islower() else c.lower() for c in s))
    return thing

#main method
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
