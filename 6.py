import urllib.request
import zipfile
import os
import re

if not os.path.exists('tmp/6'):
    os.makedirs('tmp/6')

urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', 'tmp/6/channel.zip')

file_ref = zipfile.ZipFile('tmp/6/channel.zip', 'r')
file_ref.extractall('tmp/6/channel')

comments = []

# hint1: start from 90052
# hint2: answer is inside the zip

next_nothing = '90052'

while True:
    filename = next_nothing + '.txt'
    file_contents = file_ref.read(filename).decode('UTF8')

    next_idx = re.findall(r'[0-9]', file_contents)
    if len(next_idx) == 0:
        break

    next_nothing = ''.join(next_idx)
    comment = file_ref.getinfo(filename).comment.decode('UTF8')
    comments.append(comment)
    print(file_contents)

file_ref.close()

# Collect the comments.
message = ''.join(comments)
print(message)

# Answer (1): HOCKEY
# Answer (2): OXYGEN
