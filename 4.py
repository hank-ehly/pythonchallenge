import urllib.request
import re
import math

# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
next_nothing = '12345'

for idx in range(500):
    with urllib.request.urlopen(base_url + next_nothing) as response:
        html = str(response.read())
        digits = re.findall(r'[0-9]+', html)
        print('(%d) %s' % (idx, html))

        if len(digits) == 0:
            next_nothing = str(math.floor((int(next_nothing) / 2)))
        else:
            next_nothing = digits[len(digits) - 1]

# Answer: peak.html
