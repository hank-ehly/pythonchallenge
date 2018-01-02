import pickle
import urllib.request

# Retrieved from page source
url = 'http://www.pythonchallenge.com/pc/def/banner.p'

with urllib.request.urlopen(url) as data:
    serialized_list = pickle.loads(data.read())
    message = ''
    for row in serialized_list:
        for group in row:
            char = group[0]
            repeat = group[1]
            for _ in range(repeat):
                message += char
        message += '\n'
    print(message)

# Answer: channel
